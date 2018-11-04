# -*- coding: utf-8 -*-
import scrapy
import re,os
import datetime as dt
import urllib, urllib2, json

from scrapy.exceptions import DropItem

urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])


###########################################################
class centaSpider(scrapy.Spider):
    name = 'cclhistory'
    urlToScrap = os.environ['URL_TO_SCRAP']
    scrapToDate =  dt.datetime.now()
    scrapFromDate = scrapToDate - dt.timedelta(days=40)
    #scrapFromDate = scrapToDate - dt.timedelta(days=365*30)
    start_urls = [urlToScrap]

    download_delay = 5.0
    
    ffdata ={ ## R1: v2  CCL=v2 / CCLlarge=v8 / CCLsmallMid=v9 / CCLmass=v4 / CCL district =v5
        'CCL_HK':   {'R1': 'v5', 'DropDownList3' : u"港島"},
        'CCL_KLN':  {'R1': 'v5', 'DropDownList3' : u"九龍" },
        'CCL_NTE':  {'R1': 'v5', 'DropDownList3' : u"新界(東)" },
        'CCL_NTW':  {'R1': 'v5', 'DropDownList3' : u"新界(西)" },
        'CCL_L':    {'R1': 'v8'},
        'CCL_SM':   {'R1': 'v9'},
        'CCL':      {'R1': 'v2'},
        'CCL_mass': {'R1': 'v4'},
    }
    
    #######################
    # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
    def apiGet(self, table, selectdictlist):
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
    def parse(self, response):
        #tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        # //*[@id="AutoNumber1"]/tbody/tr
        tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        if len(tbl) > 0:
            print tbl
        else:
            #for c in self.ffdata:
            if True: #True means weekly jobs
                for c in ['CCL','CCL_HK','CCL_KLN','CCL_NTE','CCL_NTW','CCL_L','CCL_SM','CCL_mass']:
                    fdate = self.scrapFromDate
                    tdate = self.scrapToDate
                    iformdata = self.ffdata[c].copy()
                    iformdata.update( { 'TextBox1' : fdate.strftime('%Y'), 'DropDownList1' : fdate.strftime('%m'), 'TextBox2' : fdate.strftime('%d')} )
                    iformdata.update( { 'TextBox3' : tdate.strftime('%Y'), 'DropDownList2' : tdate.strftime('%m'), 'TextBox4' : tdate.strftime('%d')} )
                    yield scrapy.FormRequest.from_response(
                        response,
                        formdata=iformdata,
                        callback=self.parsedata,
                        meta={'ccltype': c}
                    )
            else:
                for c in ['CCL','CCL_HK','CCL_KLN','CCL_NTE','CCL_NTW','CCL_L','CCL_SM']:
                    for y in range(1993,2019,1):
                        fdate = dt.datetime.strptime('%d/01/01' %(y),  "%Y/%m/%d")
                        tdate = fdate + dt.timedelta(days=366)
                        
                        iformdata = self.ffdata[c].copy()
                        iformdata.update( { 'TextBox1' : fdate.strftime('%Y'), 'DropDownList1' : fdate.strftime('%m'), 'TextBox2' : fdate.strftime('%d')} )
                        iformdata.update( { 'TextBox3' : tdate.strftime('%Y'), 'DropDownList2' : tdate.strftime('%m'), 'TextBox4' : tdate.strftime('%d')} )
                        yield scrapy.FormRequest.from_response(
                            response,
                            formdata=iformdata,
                            callback=self.parsedata,
                            meta={'ccltype': c}
                        )

    ################################
    def parsedata(self, response):
        trs = response.xpath('//*[@id="AutoNumber1"]//tr') #.extract()
        #print len(trs)
        for tr in trs :  #skip the header
            try:
                tds = tr.xpath('td/text()')
                [fromstr, tostr] = tds[0].extract().split('-')
                #
                rowdict = {
                    'FromDate':dt.datetime.strptime(fromstr.strip(), "%Y/%m/%d").strftime("%Y-%m-%d"),
                    'ToDate':dt.datetime.strptime(tostr.strip(),   "%Y/%m/%d").strftime("%Y-%m-%d"),
                    response.meta['ccltype'] : tds[1].extract(),
                    }
                print rowdict
                # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
                print self.apiUpsert('Centa_CCL' , [{'fld':'FromDate', 'op':'EQ', 'val':rowdict['FromDate']}], rowdict)
            except:
                pass
        print "END"
