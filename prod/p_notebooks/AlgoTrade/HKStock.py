import pymysql, talib, sys, os, tempfile
import pandas as pd , numpy as np

#############################################
class HKStock:
    conn = None
    symbol=None
    daily=None
    ####################
    def __init__(self,symbol):
        self.symbol = symbol
        self.populate()
    ####################
    def populate(self):
        if self.conn is None:
            self.conn = pymysql.connect(host='tptcn.ddns.net', port=53306, db='p_master',
                                   user=os.environ['MYSQL_READUSER'], password=os.environ['MYSQL_READPASSWORD'],
                                   cursorclass=pymysql.cursors.DictCursor)
        tmpl = "SELECT  * FROM `consolidated_daily` WHERE `symbol`='%s' "
        sql = tmpl % (self.symbol)
        self.daily= pd.read_sql(sql, self.conn, index_col=['Date'] )
        ### temp
        sOpen  = self.daily['Open']
        sHigh  = self.daily['High']
        sLow   = self.daily['Low']
        sClose = self.daily['Close']
        sVolume= self.daily['Volume']
    ####################
    def saveCSV(self,fromdate=None,todate=None):
        daily=self.daily
        if fromdate is not None: 
            daily = daily.loc[fromdate:]
        if todate is not None: 
            daily = daily.loc[:todate]
        
        tmpfilename = '/tmp/%s' %(self.symbol)
        daily.to_csv(tmpfilename, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index_label='Date Time')
        return tmpfilename

    ####################
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
