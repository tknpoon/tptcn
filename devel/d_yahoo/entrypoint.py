#!/usr/bin/python
# -*- coding: utf-8 -*-

import json,math,time,os, sys, urllib, urllib2
import datetime as dt
import pandas_datareader.data as web
from multiprocessing import Pool
import MySQLdb as my
from sqlalchemy import create_engine

## global variables

##############################
def save_sql(symbol, df):
    ##
    conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master'%(os.environ['STAGE']))
    cursor = conn.cursor()
    for index, row in df.iterrows():
        #print index,row
        stmt = """INSERT INTO yahoo_daily (symbol, Date, Open, High, Low, Close, Volume, `Adj Close`) 
            VALUES ('%s','%s',%f,%f,%f,%f,%d,%f) 
            ON DUPLICATE KEY UPDATE `Open`=%f, `High`=%f, `Low`=%f, `Close`=%f, `Volume`=%d, `Adj Close`=%f
            """ % (symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close'],
                                  row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close']
                                  )
        r = cursor.execute(stmt)
        #print "Exec result:",r
    conn.commit()
    conn.close()

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
        earliestDate = dt.datetime(1990, 1, 1)
        
    #Get a list of RIC
    symdatelist=[]
    conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master'%(os.environ['STAGE']))
    conn.query("SELECT DISTINCT `symbol` FROM `symbol_list` WHERE `yahoo_symbol` IS NOT NULL")
    r=conn.use_result()
    while (True):
        row = r.fetch_row()
        if len(row) == 0: break
        symdatelist.append( [ row[0][0] , earliestDate])
    conn.close()
    #

    #symdatelist=[]
    #symdatelist.append( ['1686.HK', earliestDate])
    #symdatelist.append( ['2318.HK', earliestDate])
    #symdatelist.append( ['0008.HK', earliestDate])
    #symdatelist.append( ['0003.HK', earliestDate])
    #print symdatelist
    
    # Grab the bars
    use_pool = False
    if use_pool :
        Pool(4).map(grabyahoo, symdatelist)
    else:
        for sd in symdatelist:
            #print sd
            grabyahoo(sd)

