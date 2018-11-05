#!/usr/bin/python
# -*- coding: utf-8 -*-

import json,math,time,os, sys, urllib, urllib2
import datetime as dt
import pandas_datareader.data as web
from multiprocessing import Pool
import MySQLdb as my
from sqlalchemy import create_engine

## global variables

urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])

##############################
def save_sql(symbol, df):
    ##
    conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master'%(os.environ['STAGE']))
    cursor = conn.cursor()
    for index, row in df.iterrows():
        #print index,row
        stmt = """REPLACE INTO yahoo_daily (symbol, Date, Open, High, Low, Close, Volume, `Adj Close`) 
            VALUES ('%s','%s',%f,%f,%f,%f,%d,%f)
            """ % (symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close'])
        #print stmt
        r = cursor.execute(stmt)
        #print "Exec result:",r
    conn.commit()
    conn.close()

#######################
# selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
def apiGet(table, selectdictlist):
    querylist=[]
    for dict in selectdictlist:
        querylist.append("%s[%s]=%s" %(dict['fld'], dict['op'], dict['val']))
    url = "%s/%s?%s" % (urlbase,table, '&'.join(querylist))
    # print url
    req = urllib2.Request(url)
    try :
        response = urllib2.urlopen(req)
        return json.loads(response.read())
    except urllib2.HTTPError:
        return {}
        
########################
# selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
# valuedict : {fld : value, fld, value, ...}
def apiUpsert(table, selectdictlist, valuedict):
    centaResult = apiGet(table, selectdictlist )
    # print centaResult
    if 'result' in centaResult: #found, update with PUT
        for row in centaResult['json']:
            url = "%s/%s/%d" % (urlbase ,table, row['ID'])
            # print url, urllib.urlencode(valuedict)
            req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
            req.get_method = lambda: 'PUT'
            response = urllib2.urlopen(req)
            return json.loads( response.read())
    else: #not found, insert with POST
        url = "%s/%s" % (urlbase ,table)
        # print url, urllib.urlencode(valuedict)
        req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
        req.get_method = lambda: 'POST'
        response = urllib2.urlopen(req)
        return json.loads( response.read())


##############################
def grabyahoo(symbol_date):
    [symbol,start_date] = symbol_date
    
    source='yahoo'

    toDate = dt.datetime.today()
    
    totalRows = 0
    while (start_date < toDate ) :
        fromDate = toDate - dt.timedelta(days=70)
        
        qt = None
        try:
            qt= web.DataReader(symbol, source, fromDate.strftime('%m/%d/%Y'), toDate.strftime('%m/%d/%Y'))
            qt.dropna(inplace = True)
        except:
            qt = None
        ##
        if qt is not None and len(qt.index) > 0:
            totalRows = totalRows + len(qt.index)
            #print symbol, len(qt.index)
            save_sql(symbol, qt)
        else:
            break

        print "Getting", symbol, fromDate, toDate, totalRows, "rows."
        toDate = fromDate
    print "Got", symbol, "from", start_date, totalRows, "rows."
    return symbol

    
##############################
# main
if __name__ == '__main__':
    earliestDate = dt.datetime.today() - dt.timedelta(days=10)
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        earliestDate = dt.date(1990, 1, 1)
        #earliestDate = dt.date(2017, 1, 1)
        
    #Get a list of RIC
    symdatelist=[]
    result= apiGet('hkex_listings', {})
    if 'result' in result:
        for row in result['json']:
            symdatelist.append( [row['symbol'] , earliestDate])
            
    #symdatelist=[]
    #symdatelist.append( ['1686.HK', earliestDate])
    #symdatelist.append( ['2318.HK', earliestDate])
    #symdatelist.append( ['0008.HK', earliestDate])
    #symdatelist.append( ['0003.HK', earliestDate])
    #print symdatelist
    
    # Grab the bars
    use_pool = True
    if use_pool :
        Pool(4).map(grabyahoo, symdatelist)
    else:
        for sd in symdatelist:
            grabyahoo(sd)

