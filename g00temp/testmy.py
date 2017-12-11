#!/usr/bin/python

import json,math,time,os
import datetime as dt
#import _mysql as my
import MySQLdb as my

import pandas_datareader.data as web
from multiprocessing import Pool

##############################
def grabyahoo(symbol):
    source='yahoo'
    start='01/01/1990'
    end=dt.date.today().strftime('%m/%d/%Y')
    qt= web.DataReader(symbol, source, start, end)
    print qt.tail()
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
        
    p = Pool(3)
    print(p.map(grabyahoo, symlist))
    
#while (True) :
#    row = r.fetch_row()
#    if len(row) == 0: break
#
#    symbol = row[0][0]
#
#    source='yahoo'
#    start='01/01/1990'
#    end='01/01/2018'
#    
#    qt= web.DataReader(symbol, source, start, end)
#    print qt.tail()
#
#    time.sleep(1)
#
#conn.close()
#
#
#
#
#