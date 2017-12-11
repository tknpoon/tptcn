#!/usr/bin/python

import json,math,time,os
import datetime as dt
#import _mysql as my
import MySQLdb as my

import pandas_datareader.data as web
from multiprocessing import Pool
from sqlalchemy import create_engine

##############################
def grabyahoo(symbol):
    source='yahoo'
    start='01/01/1990'
    end=dt.date.today().strftime('%m/%d/%Y')
    ##
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    conn.query("select max(Date) from tDailyPrice_yahoo where symbol = '%s' " % (symbol) )
    r=conn.use_result()
    while (True) :
        row = r.fetch_row()
        if len(row) == 0 or row[0][0] is None: break
        start= row[0][0].strftime('%m/%d/%Y')
    conn.close()
    qt= web.DataReader(symbol, source, start, end)
    qt.dropna(inplace = True)
    
    ##
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    cursor = conn.cursor()
    for index, row in qt.iterrows():
        #print index,row
        stmt = """REPLACE INTO tDailyPrice_yahoo (symbol, Date, Open, High, Low, Close, Volume, `Adj Close`) 
            VALUES ('%s','%s',%f,%f,%f,%f,%d,%f)
            """ % (symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close'])
        #print stmt
        r = cursor.execute(stmt)
        #print "Exec result:",r
        conn.commit()
        
    conn.close()
    return symbol

    
##############################
# main
if __name__ == '__main__':
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    conn.query("select symbol from tSymbol where availVendors like '%test%' ")
    r=conn.use_result()
    
    symlist=[]
    while (True) :
        row = r.fetch_row()
        if len(row) == 0: break
        symlist.append(row[0][0])
    conn.close()
        
#    p = Pool(3)
#    print(p.map(grabyahoo, symlist))
    for s in symlist:
        grabyahoo(s)
