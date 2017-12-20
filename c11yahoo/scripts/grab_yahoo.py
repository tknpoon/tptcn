#!/usr/bin/python

import json,math,time,os, sys
import datetime as dt
#import _mysql as my
import MySQLdb as my

import pandas_datareader.data as web
from multiprocessing import Pool
from sqlalchemy import create_engine

## global variables
grabAll = False

##############################
def save_sql(symbol, df):
    ##
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    cursor = conn.cursor()
    for index, row in df.iterrows():
        #print index,row
        stmt = """REPLACE INTO tDailyPrice_yahoo (symbol, Date, Open, High, Low, Close, Volume, `Adj Close`) 
            VALUES ('%s','%s',%f,%f,%f,%f,%d,%f)
            """ % (symbol, index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close'])
        #print stmt
        r = cursor.execute(stmt)
        #print "Exec result:",r
    conn.commit()
    conn.close()

##############################
def grabyahoo(symbol):
    source='yahoo'
    start='01/01/1990'
    end=dt.date.today().strftime('%m/%d/%Y')
    ##
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    if not grabAll:
        conn.query("select max(Date) from tDailyPrice_yahoo where symbol = '%s' " % (symbol) )
        r=conn.use_result()
        while (True) :
            row = r.fetch_row()
            if len(row) == 0 or row[0][0] is None: break
            start= row[0][0].strftime('%m/%d/%Y')
        conn.close()

    try:
        qt= web.DataReader(symbol, source, start, end)
        qt.dropna(inplace = True)
        print symbol, len(qt.index)
        ##
        save_sql(symbol, qt)
        return symbol
    except:
        print "Failed to get", symbol
        return None

    
##############################
# main
if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == "all":
        grabAll = True

    #Get a list of RIC
    symlist=[]
    conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
    conn.query("select symbol from tSymbol where availVendors like '%yahoo%' ")
    r=conn.use_result()
    
    while (True):
        row = r.fetch_row()
        if len(row) == 0: break
        symlist.append(row[0][0])
    conn.close()

    # Grab the bars
    use_pool = True
    if use_pool :
        Pool(4).map(grabyahoo, symlist)
    else:
        for s in symlist:
            grabyahoo(s)
