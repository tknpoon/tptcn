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
    #if sym != '2388.HK': continue
    print sym
    df = getOHLCV(sym)
    #print df
    #
    dfClose=df['Close'].dropna()
    if len(dfClose) <= 100: continue
    
    ta = talib.RSI(dfClose, timeperiod=14)
    ta_Mean = ta.rolling(100,100).mean()
    ta_SD = talib.STDDEV(ta, timeperiod=100)
    #
    df['RSI'] = ta
    df['RSI_mean'] = ta_Mean
    df['RSI_sd'] = ta_SD
    #
    saveDF(sym, df, ['RSI', 'RSI_mean','RSI_sd'])
