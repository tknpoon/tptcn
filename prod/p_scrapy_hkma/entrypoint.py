import scrapy
import re,os, json, urllib,urllib2
import datetime as dt

################################

class hkmaSpider(scrapy.Spider):
    name = 'hkma'
    urlbase = "http://%s_dbapi:3000/api" %(os.environ['STAGE'])

    urlToScrap = os.environ['URL_TO_SCRAP']
    thedate = dt.datetime.strptime(os.path.basename(urlToScrap)[9:17], '%Y%m%d')
    #start_urls = [dt.datetime.today().strftime('http://web/raw/hkma/%Y/moneybase%Y%m%d-2.html')]
    start_urls = [urlToScrap]
    
    ################################
    def parse(self, response):
        thelist= self.parseNow(response)
        return self.saveDay(thelist)
        
    ################################
    def parseNow(self, response):
        table= response.xpath('//*[contains(text(),"Total")]/ancestor::table')
        if len(table)== 0:
            table= response.xpath('//*[contains(text(),"TOTAL")]/ancestor::table')
        return [
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[2]//td').extract()[-2].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[2]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[3]//td').extract()[-2].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[3]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[4]//td').extract()[-2].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[4]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[5]//td').extract()[-2].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[5]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[6]//td').extract()[-2].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[6]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower())),
            self.striptag(re.sub('mn.*$', '', table.xpath('.//tr[7]//td').extract()[-1].encode("utf-8").replace('\r','').replace('\n','').lower()))
        ]

    ################################
    def striptag(self, thestr):
        #print "====================="
        tmpstr = thestr
        #print "@@@@",tmpstr
        while ( '<' in tmpstr) :
            tmpstr = re.sub('\<[^\>]*\>' , '' , tmpstr)
        #    print "@@@@",tmpstr
        tmpstr = re.sub('[^0-9]' , '' , tmpstr)
        #print "@@@@",tmpstr

        return tmpstr
        
    #######################
    # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
    def apiGet(self, table, selectdictlist):
        querylist=[]
        for dict in selectdictlist:
            querylist.append("%s[%s]=%s" %(dict['fld'], dict['op'], dict['val']))
        url = "%s/%s?%s" % (self.urlbase, table, '&'.join(querylist))
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
        selectResult = self.apiGet(table, selectdictlist )
        print selectResult
        if 'result' in selectResult: #found, update with PUT
            for row in selectResult['json']:
                url = "%s/%s/%d" % (self.urlbase ,table, row['ID'])
                # print url, urllib.urlencode(valuedict)
                req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
                req.get_method = lambda: 'PUT'
                response = urllib2.urlopen(req)
                return json.loads( response.read())
        else: #not found, insert with POST
            url = "%s/%s" % (self.urlbase ,table)
            # print url, urllib.urlencode(valuedict)
            req = urllib2.Request(url, data=urllib.urlencode(valuedict), headers={'Content-type':'application/x-www-form-urlencoded'} )
            req.get_method = lambda: 'POST'
            response = urllib2.urlopen(req)
            return json.loads( response.read())

    ################################################################
    def saveDay(self, dlist):
        [
            CertIndebtAfterDisc, CertIndebtBeforeDisc,
            GovtCirAfterDisc, GovtCirBeforeDisc, 
            CloseAggBalAfterDisc, CloseAggBalBeforeDisc, 
            OutstandEFNAfterDisc, OutstandEFNBeforeDisc, 
            OutstandEFNBankAfterDisc, OutstandEFNBankBeforeDisc,
            Total
        ] = dlist
        print dlist
        valuedict = {
            'Date' : self.thedate.strftime('%Y-%m-%d'),
            'CertIndebtAfterDisc' : CertIndebtAfterDisc,
            'CertIndebtBeforeDisc' : CertIndebtBeforeDisc,
            'GovtCirAfterDisc' : GovtCirAfterDisc,
            'GovtCirBeforeDisc' : GovtCirBeforeDisc,
            'CloseAggBalAfterDisc' : CloseAggBalAfterDisc,
            'CloseAggBalBeforeDisc' : CloseAggBalBeforeDisc,
            'OutstandEFNAfterDisc' : OutstandEFNAfterDisc,
            'OutstandEFNBeforeDisc' : OutstandEFNBeforeDisc,
            'OutstandEFNBankAfterDisc' : OutstandEFNBankAfterDisc,
            'OutstandEFNBankBeforeDisc' : OutstandEFNBankBeforeDisc,
            'Total' : Total,
        }
        print valuedict
    
        # selectdictlist : [ {fld : colname, op : EQ, val : value } , ... ]
        # valuedict : {fld : value, fld, value, ...}
        self.apiUpsert('hkma_bal', [{'fld':'Date', 'op':'EQ', 'val':self.thedate.strftime('%Y-%m-%d')}], valuedict)
