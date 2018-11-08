# -*- coding: utf-8 -*-
import scrapy
import re,os
import datetime as dt
import urllib, urllib2, json

from scrapy.exceptions import DropItem

urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])


###########################################################
class tester():
    #######################
    # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
    def apiGet(self, table, selectdictlist):
        querylist=[]
        for dict in selectdictlist:
            querylist.append("%s[%s]=%s" %(dict['fld'], dict['op'], dict['val']))
        url = "%s/%s?%s" % (urlbase,table, '&'.join(querylist))
        print url
        req = urllib2.Request(url)
        try :
            response = urllib2.urlopen(req)
            return json.loads(response.read())
        except urllib2.HTTPError:
            print "he"
            return {}

    ################################
    def getget(self):
        j = self.apiGet("Centa_CCL", [
                #{'fld':'ID','op':'EQGREAT','val':1},
                {'fld':'FromDate','op':'EQ','val':'2018-10-01'},
            ] )
        #print j
        if 'result' in j:
            for i in j['json'] :
                print i
                pass
        else:
            print "END"

    ########################
    # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
    # valuedict : {fld : value, fld, value, ...}
    def apiUpsert(self, table, selectdictlist, valuedict):
        centaResult = self.apiGet(table, selectdictlist )
        # print centaResult
        if 'result' in centaResult: #found, update with PUT
            for row in centaResult['json']:
                url = "%s/%s/%d" % (urlbase ,table, row['ID'])
                # print url, urllib.urlencode(valuedict)
                req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
                req.get_method = lambda: 'PUT'
                response = urllib2.urlopen(req)
                return json.loads( response.read())
        else: #not found, insert with POST
            url = "%s/%s" % (urlbase ,table)
            # print url, urllib.urlencode(valuedict)
            req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
            req.get_method = lambda: 'POST'
            response = urllib2.urlopen(req)
            return json.loads( response.read())

    ################################
    def upsert(self):
        j = self.apiUpsert("Centa_CCL", 
            [  {'fld':'FromDate','op':'EQ','val':'2018-10-15'}],
            {'FromDate':'2018-10-15','ToDate':'2018-10-22', 'CCL':3 }
        )
        #print j
        if 'result' in j:
            for i in j['json'] :
                print i
                pass
        else:
            print "END"

################################
t = tester()
# t.getget()
t.upsert()
