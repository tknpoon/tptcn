import datetime as dt
import pymysql, talib, sys, os, tempfile
import pandas as pd , numpy as np

#############################################
class HKYahoo:
    conn = None
    symbol=None
    
    daily=None
    weekly=None
    monthly=None
    yearly=None
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

        tmpl = "SELECT  * FROM `yahoo_daily` WHERE `symbol`='%s' "
        sql = tmpl % (self.symbol)
        self.daily= pd.read_sql(sql, self.conn, index_col=['Date'] )
        
        ### roll up 
        tmpdf = self.daily
        tmpdf = tmpdf.reset_index()

        tmpdf['Date'] = pd.to_datetime(tmpdf['Date'])

        tmpdf['yyyymm'] = tmpdf['Date'].dt.strftime("%Y%m")
        tmpdf['Month_Number'] = tmpdf['Date'].dt.month
        tmpdf['Year'] = tmpdf['Date'].dt.year

        # 'daysoffset' will container the weekday, as integers
        tmpdf['daysoffset'] = tmpdf['Date'].apply(lambda x: x.weekday())
        # We apply, row by row (axis=1) a timedelta operation
        tmpdf['week_start'] = tmpdf.apply(lambda x: x['Date'] - dt.timedelta(days=x['daysoffset']), axis=1)

        ### weekly
        self.weekly = tmpdf.groupby(['week_start']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum','Adj Close':'last'})
        self.weekly['Count'] =tmpdf.groupby(['week_start']).size()
        self.weekly = self.weekly.reset_index().set_index('week_start')[['Open','High','Low','Close','Volume','Adj Close','Count']]

        ### monthly
        self.monthly = tmpdf.groupby(['Year','Month_Number']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum','Adj Close':'last', 'yyyymm':'first'})
        self.monthly['Count'] =tmpdf.groupby(['Year','Month_Number']).size()
        self.monthly = self.monthly.reset_index().set_index('yyyymm')[['Open','High','Low','Close','Volume','Adj Close','Count']]

        ### yearly
        self.yearly = tmpdf.groupby(['Year']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum','Adj Close':'last'})
        self.yearly['Count'] =tmpdf.groupby(['Year']).size()
        self.yearly = self.yearly[['Open','High','Low','Close','Volume','Adj Close','Count']]


    ####################
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
