#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import re,os, json, urllib,urllib2
import datetime as dt
import MySQLdb as my

################################

class hkmaSpider(scrapy.Spider):
    name = 'hkma'

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
    
        conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master' % (os.environ['STAGE']))
        cursor = conn.cursor()
        
        placeholders = ', '.join(['%s'] * len(valuedict))
        columns = ', '.join(valuedict.keys())
        stmt = "REPLACE INTO %s ( %s ) VALUES ( %s )" % ('hkma_bal', columns, placeholders)
        
        print stmt
        try:
            r= cursor.execute(stmt, valuedict.values())
        except Exception, e:
            print "EXCEPTION", e
            raise
        print "Done!"
        conn.commit()
        conn.close()
