#!/usr/bin/python
import zipfile, os, re, pymysql, glob,json, time, sys
import datetime as dt

import requests                  # [handles the http interactions](http://docs.python-requests.org/en/master/) 
from bs4 import BeautifulSoup    # beautiful soup handles the html to text conversion and more
import re                        # regular expressions are necessary for finding the crumb (more on crumbs later)
#from datetime import timedelta,datetime    # string to datetime object conversion
from time import mktime          # mktime transforms datetime objects to unix timestamps

#################################
def saveYahoo(symbol,lists):
    #print   symbol
    conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
            user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
    cursor = conn.cursor()
    stmts=[]
    cols=[]
    for l in lists:
        l = l.strip()
        if len(cols) == 0:
            cols=['symbol']
            cols.extend( l.split(',') )
            #print cols
        else:
            vlist=l.split(',')
            stmts.append("REPLACE INTO `yahoo_daily` (%s) VALUES ('%s','%s',%s);" 
                % ( ','.join("`{0}`".format(w) for w in cols),
                symbol, vlist[0], ','.join(vlist[1:]))
                )

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
def getSymList():
    symbollist=[]
    stmt="""
        SELECT `symbol` FROM `hkex_quotation`
        WHERE `Date` IN (SELECT MAX(`Date`) FROM `hkex_quotation`)
        AND `Volume` IS NOT NULL
        AND `ShortVolume` IS NOT NULL
    """
    conn = pymysql.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master'%(os.environ['STAGE']))
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(stmt)
    for row in cur:
        symbollist.append( row['symbol'] )
    conn.close()
    #
    return symbollist


########################################################
def _get_crumbs_and_cookies(stock):
    """
    get crumb and cookies for historical data csv download from yahoo finance
    parameters: stock - short-handle identifier of the company 
    returns a tuple of header, crumb and cookie
    """
    
    url = 'https://finance.yahoo.com/quote/{}/history'.format(stock)
    with requests.session():
        header = {'Connection': 'keep-alive',
                   'Expires': '-1',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                   }
        
        website = requests.get(url, headers=header)
        soup = BeautifulSoup(website.text, 'lxml')
        crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))

        return (header, crumb[0], website.cookies)


########################################################
def convert_to_unix(date):
    """
    converts date to unix timestamp
    parameters: date - in format (dd-mm-yyyy)
    returns integer unix timestamp
    """
    datum = dt.datetime.strptime(date, '%d-%m-%Y')
    return int(mktime(datum.timetuple()))


########################################################
def load_csv_data(stock, interval='1d', day_begin=(dt.datetime.now()-dt.timedelta(days=14)).strftime('%d-%m-%Y'), day_end=dt.datetime.now().strftime('%d-%m-%Y')):
    """
    queries yahoo finance api to receive historical data in csv file format
    parameters: 
        stock - short-handle identifier of the company
        interval - 1d, 1wk, 1mo - daily, weekly monthly data
        day_begin - starting date for the historical data (format: dd-mm-yyyy)
        day_end - final date of the data (format: dd-mm-yyyy)
    returns a list of comma seperated value lines
    """
    day_begin_unix = convert_to_unix(day_begin)
    day_end_unix = convert_to_unix(day_end)
    
    trycount=0
    while trycount<5: #max try 5 times
        trycount = trycount + 1
        header, crumb, cookies = _get_crumbs_and_cookies(stock)
        with requests.session():
            url = 'https://query1.finance.yahoo.com/v7/finance/download/' \
                  '{stock}?period1={day_begin}&period2={day_end}&interval={interval}&events=history&crumb={crumb}' \
                  .format(stock=stock, day_begin=day_begin_unix, day_end=day_end_unix, interval=interval, crumb=crumb)
                    
            website = requests.get(url, headers=header, cookies=cookies)
            try:
                j = json.loads(website.text) #success load json string --> error 
                print stock, "try again!!!!!!, trycount=" , trycount
                print website.text
                time.sleep(2)
            except ValueError,e:
                return website.text.split('\n')[:-1]
    return None

#################################
## main
begindate=(dt.datetime.now()-dt.timedelta(days=7)).strftime('%d-%m-%Y')
if len(sys.argv) > 1:
    begindate=sys.argv[1]

slist = getSymList()
for s in slist:
    csv = load_csv_data(s, day_begin=begindate)
    #csv = load_csv_data(s)
    if csv is not None:
        saveYahoo(s,csv)
