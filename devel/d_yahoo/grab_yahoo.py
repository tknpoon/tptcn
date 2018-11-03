#!/usr/bin/python
# -*- coding: utf-8 -*-

import json,math,time,os, sys, urllib, urllib2
import datetime as dt
import pandas_datareader.data as web
from multiprocessing import Pool

## global variables

urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])

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
    [symbol,startdate] = symbol_date
    
    source='yahoo'
    end=dt.date.today().strftime('%m/%d/%Y')
    ##
    qt = None
    try:
        qt= web.DataReader(symbol, source, startdate, end)
        qt.dropna(inplace = True)
        #print qt
    except:
        print "Failed to get", symbol, source, startdate, end
        return None
    #print symbol, len(qt.index)
    ##
    if qt is not None:
        df = qt.reset_index()
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        dd = df.to_dict('records')
        
        for d in  dd:
            selectlist= [   {'fld':'Date', 'op':'EQ', 'val':d['Date']},
                            {'fld':'symbol', 'op':'EQ', 'val':symbol},
                        ]
            #print selectlist
            d['symbol'] = symbol
            upsertresult = apiUpsert('yahoo_daily' , selectlist, d)
            print upsertresult['result'] if 'result' in upsertresult else "failed" , "upsert", selectlist

    return symbol

    
##############################
# main
if __name__ == '__main__':
    startdate = (dt.datetime.today() - dt.timedelta(days=30)).strftime('%Y-%m-%d')
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        startdate = '1990-01-01'
    
    #Get a list of RIC
    symdatelist=[]
    result= apiGet('hkex_listings', {})
    if 'result' in result:
        for row in result['json']:
            symdatelist.append( [row['symbol'] , startdate])
            
    print symdatelist
    
    
    # Grab the bars
    use_pool = True
    if use_pool :
        Pool(4).map(grabyahoo, symdatelist)
    else:
        for sd in symdatelist:
            grabyahoo(sd)

