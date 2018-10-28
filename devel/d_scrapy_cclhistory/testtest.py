# -*- coding: utf-8 -*-
import re,os
import datetime as dt
import urllib, urllib2, json

url = "http://d_xmysql:3000/api/tTest"
thedata='Date=2018-10-01&symbol=tt&a=4&b=4&c=4&d=4'

########################
#req = urllib2.Request(url, thedata, headers={'Content-type': 'application/x-www-form-urlencoded'})
req = urllib2.Request(url)
#req.get_method = lambda: 'PUT'

response = urllib2.urlopen(req)
the_page = response.read()

jpage = json.loads( the_page)
print json.dumps(jpage, indent=4, separators=(',', ': '))

########################
req = urllib2.Request(url, thedata, headers={'Content-type': 'application/x-www-form-urlencoded'})
req.get_method = lambda: 'PUT'

response = urllib2.urlopen(req)
the_page = response.read()

jpage = json.loads( the_page)
print json.dumps(jpage, indent=4, separators=(',', ': '))

########################
#req = urllib2.Request(url, thedata, headers={'Content-type': 'application/x-www-form-urlencoded'})
req = urllib2.Request(url)
#req.get_method = lambda: 'PUT'

response = urllib2.urlopen(req)
the_page = response.read()

jpage = json.loads( the_page)
print json.dumps(jpage, indent=4, separators=(',', ': '))
