#!/usr/bin/python

import json,math,time,os
import datetime as dt
#import _mysql as my
import MySQLdb as my

import pandas_datareader.data as web


conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])

conn.query("""
select symbol from tSymbol where availVendors like "%test%"
""")
r=conn.use_result()

######
while (True) :
    row = r.fetch_row()
    if len(row) == 0: break

    symbol = row[0][0]

    source='yahoo'
    start='01/01/1990'
    end='01/01/2018'
    
    qt= web.DataReader(symbol, source, start, end)
    print qt.tail()

    time.sleep(1)

conn.close()




