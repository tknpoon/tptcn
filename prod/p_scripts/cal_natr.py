#!/usr/bin/python
import pymysql, talib, os, re
import numpy as np
import pandas as pd
import datetime as dt

#################################
def getSymbols():
    conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
            user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
    cursor = conn.cursor()
    sql="""
    SELECT DISTINCT `symbol` FROM `consolidated_daily`
    """
    df = pd.read_sql(sql, conn)
    #conn.commit()
    conn.close()
    return df['symbol'].tolist()

#################################
def getOHLCV(symbol):
    conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
            user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
    cursor = conn.cursor()
    sql="""
    SELECT `Date`,`Open`,`High`,`Low`,`Close`,`Volume` FROM `consolidated_daily` WHERE `symbol`="%s"
    """ % (symbol)
    df = pd.read_sql(sql, conn, index_col=['Date'])
    #conn.commit()
    conn.close()
    return df

#################################
def saveDF(symbol, df_ta, fldlist):
        conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
                user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
        cursor = conn.cursor()
        
        stmts=[]
        for index, row in df_ta.iterrows():  #index is the Date
            for fld in fldlist:
                sql="""UPDATE `consolidated_daily` SET `%s`=%s
                WHERE `%s`='%s' AND `%s`='%s' ;
                """ % (fld,  'NULL' if pd.isnull(row[fld]) else round(row[fld],3)  ,
                'symbol',symbol, 'Date',index)
                stmts.append(sql)

        for stmt in stmts:
            try:
                #print stmt
                r= cursor.execute(stmt)
            except Exception, e:
                print "EXCEPTION", e
                print stmt
                raise
        conn.commit()
        conn.close()
        return    

#################################
## main
sList = getSymbols()
for sym in sList:
    df = getOHLCV(sym)
    #
    df['NATR_10'] = talib.NATR(df['High'], df['Low'], df['Close'], timeperiod=10)
    saveDF(sym, df, ['NATR_10'])
