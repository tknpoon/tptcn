#!/usr/bin/python

import json,math,time,os, sys, urllib,urllib2
import datetime as dt

import pandas_datareader.data as web

from multiprocessing import Pool

## global variables
grabAll = False
urlbase = "http://d_xmysqlrw:3000/api"

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

########################
def apiget(table, dict):
    #print table, urllib.urlencode(dict)
    i=0
    querystr=""
    for elem in dict:
        if i == 0:
            querystr = "_where=(%s,eq,%s)" %(elem, dict[elem])
        else:
            querystr = querystr + "~and(%s,eq,%s)" %(elem, dict[elem])
        i = i + 1
    url = "%s/%s?_p=2&_size=50&_fields=symbol" % (urlbase,table)
    print url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()

    return json.loads(the_page)
##############################
#grabyahoo('0005.HK')
rics= apiget('hkex_listings',{})
print len(rics)

