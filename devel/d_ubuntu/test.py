#!/usr/bin/python

import json,math,time,os, sys, urllib,urllib2
import datetime as dt

import pandas_datareader.data as web

from multiprocessing import Pool

## global variables
grabAll = False
urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])

##############################
def grabyahoo(symbol):
    source='yahoo'
    start='01/01/1990'
    end=dt.date.today().strftime('%m/%d/%Y')
    ##
    try:
        qt= web.DataReader(symbol, source, start, end)
        qt.dropna(inplace = True)
        print symbol, len(qt.index)
        ##
        return symbol
    except:
        print "Failed to get", symbol, source, start, end
        return None

#######################
# selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
def apiGet(table, selectdictlist):
    querylist=[]
    for dict in selectdictlist:
        querylist.append("%s[%s]=%s" %(dict['fld'], dict['op'], dict['val']))
    url = "%s/%s?%s" % (urlbase,table, '&'.join(querylist))
    # print url
    req = urllib2.Request(url)
    try :
        response = urllib2.urlopen(req)
        return json.loads(response.read())
    except urllib2.HTTPError:
        return {}

##############################
#grabyahoo('0005.HK')
result= apiGet('hkex_listings', {})
if 'result' in result:
    for row in result['json']:
        print row['symbol']


