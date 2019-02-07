import datetime as dt
import pymysql, talib, sys, os, tempfile
import pandas as pd , numpy as np

#############################################
class HKta:
    conn = None
    symbol=None
    
    raw=None
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

        tmpl = "SELECT  * FROM `consolidated_daily` WHERE `symbol`='%s' "
        sql = tmpl % (self.symbol)
        self.raw= pd.read_sql(sql, self.conn, index_col=['Date'] )[['Open', 'High', 'Low', 'Close', 'Volume']]
        ### drop NA 
        self.daily = self.raw.fillna(0)
        self.daily['Volume'] = self.daily['Volume'].astype('int')
        self.daily = self.daily[self.daily['Volume'] > 0]
        self.daily = self.daily.reset_index()
        self.daily['Date'] = pd.to_datetime(self.daily['Date'])
        self.daily=self.daily.set_index('Date')

        #Close should be official; so adjust High/Low if necessary
        self.daily['High'] = np.where(self.daily['Close'] > self.daily['High'], self.daily['Close'], self.daily['High'])
        self.daily['Low']  = np.where(self.daily['Close'] < self.daily['Low'],  self.daily['Close'], self.daily['Low'])
        #Open is calculated; so, adjust according to the High/Low if necessary
        self.daily['Open'] = np.where(self.daily['Open']  > self.daily['High'], self.daily['High'],  self.daily['Open'])
        self.daily['Open'] = np.where(self.daily['Open']  < self.daily['Low'],  self.daily['Low'],   self.daily['Open'])
         
        ### roll up 
        tmpdf = self.daily
        tmpdf = tmpdf.reset_index()

        tmpdf['yyyymm'] = tmpdf['Date'].dt.strftime("%Y%m")
        tmpdf['Month_Number'] = tmpdf['Date'].dt.month
        tmpdf['Year'] = tmpdf['Date'].dt.year

        # 'daysoffset' will container the weekday, as integers
        tmpdf['daysoffset'] = tmpdf['Date'].apply(lambda x: x.weekday())
        # We apply, row by row (axis=1) a timedelta operation
        tmpdf['WeekStart'] = tmpdf.apply(lambda x: x['Date'] - dt.timedelta(days=x['daysoffset']), axis=1)

        ### weekly
        self.weekly = tmpdf.groupby(['WeekStart']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum'})
        self.weekly['Count'] =tmpdf.groupby(['WeekStart']).size()
        self.weekly['Volume'] = self.weekly['Volume'].astype('int')
        self.weekly['AvgDVol'] = (self.weekly['Volume'] / self.weekly['Count']).astype('int')
        self.weekly = self.weekly.reset_index().set_index('WeekStart')[['Open', 'High', 'Low', 'Close', 'Volume', 'AvgDVol', 'Count']]

        ### monthly
        self.monthly = tmpdf.groupby(['Year','Month_Number']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum', 'yyyymm':'first'})
        self.monthly['Count'] =tmpdf.groupby(['Year','Month_Number']).size()
        self.monthly['Volume'] = self.monthly['Volume'].astype('int')
        self.monthly['AvgDVol'] = (self.monthly['Volume'] / self.monthly['Count']).astype('int')
        self.monthly = self.monthly.reset_index().set_index('yyyymm')[['Open', 'High', 'Low', 'Close', 'Volume', 'AvgDVol', 'Count']]

        ### yearly
        self.yearly = tmpdf.groupby(['Year']).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume':'sum'})
        self.yearly['Count'] =tmpdf.groupby(['Year']).size()
        self.yearly['Volume'] = self.yearly['Volume'].astype('int')
        self.yearly['AvgDVol'] = (self.yearly['Volume'] / self.yearly['Count']).astype('int')
        self.yearly = self.yearly[['Open', 'High', 'Low', 'Close', 'Volume', 'AvgDVol', 'Count']]


    ####################
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
