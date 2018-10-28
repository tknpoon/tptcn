# -*- coding: utf-8 -*-
import re,os
import datetime as dt
import urllib, urllib2, json

urlbase = "http://d_xmysql:3000/api"

########################
def apidelete(table, dict):
    selected = apiget(table, dict)
    #print selected
    if len(selected) <= 0: 
        return []

    IDs = [r['ID'] for r in selected]
    #print IDs,   ','.join(str(v) for v in IDs)
    url = "%s/%s/bulk?_ids=%s" % (urlbase ,table,  ','.join(str(v) for v in IDs)  )
    #print url
    req = urllib2.Request(url)
    req.get_method = lambda: 'DELETE'
    
    response = urllib2.urlopen(req)
    the_page = response.read()

    return json.loads( the_page)

########################
def apiupdate(table, dict):
    selected = apiget(table, {k: dict[k] for k in ('Date', 'symbol') } )
    #print selected
    
    if len(selected) == 0:
        #print "POST"
        url = "%s/%s" % (urlbase ,table)
        req = urllib2.Request(url, data=urllib.urlencode(dict), headers={'Content-type':'application/x-www-form-urlencoded'} )
        req.get_method = lambda: 'POST'
        response = urllib2.urlopen(req)
        the_page = response.read()
        return json.loads( the_page)
    elif len(selected) == 1: 
        #print "PATCH"
        url = "%s/%s/%d" % (urlbase ,table, selected[0]['ID'] )
        newvalues = {k: dict[k] for k in dict if k not in ('Date', 'symbol', 'ID') } 
        #print newvalues
        #{key: a[key] for key in a if key not in keys}
        req = urllib2.Request(url, data=urllib.urlencode(newvalues), headers={'Content-type':'application/x-www-form-urlencoded'} )
        req.get_method = lambda: 'PATCH'
        response = urllib2.urlopen(req)
        the_page = response.read()
        return json.loads( the_page)
    else:
        return []

########################
def apiget(table, dict):
    i=0
    querystr=""
    for elem in dict:
        if i == 0:
            querystr = "_where=(%s,eq,%s)" %(elem, dict[elem])
        else:
            querystr = querystr + "~and(%s,eq,%s)" %(elem, dict[elem])
        i = i + 1
    url = "%s/%s?%s" % (urlbase,table,querystr)

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()

    return json.loads(the_page)
    

########################
ddd = 999
thedata={'Date': '2018-10-11', 'symbol':'tt3', 'a':ddd, 'b':ddd, 'c':ddd, 'd':ddd}

#jjs = apidelete('tTest', {})
#print json.dumps(jjs, indent=4, separators=(',', ': '))

pp = apiupdate('tTest', thedata)
print json.dumps(pp, indent=4, separators=(',', ': '))

jjs = apiget('tTest', {})
print json.dumps(jjs, indent=4, separators=(',', ': '))

