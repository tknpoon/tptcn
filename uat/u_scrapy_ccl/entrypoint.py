#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import re,os
import datetime as dt
import MySQLdb as my

class centaSpider(scrapy.Spider):
    name = 'centa'
    urlToScrap = os.environ['URL_TO_SCRAP']
    start_urls = [urlToScrap]
    
    ################################
    def parse(self, response):
        dateSent= response.xpath('//b[text()[contains(.,"Centa-City Leading Index CCL")]]/../..//text()').extract()[5]
        date_search = re.search('residential property price from (\S+) to (\S+) ', dateSent, re.IGNORECASE)
        if date_search:
            sdate = dt.datetime.strptime(date_search.group(1), '%Y/%m/%d')
            edate = dt.datetime.strptime(date_search.group(2), '%Y/%m/%d')
            print "-->",sdate,edate
            ccl= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
            cclLarge= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City (large units) Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
            cclSmallMedium= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City (small/medium units) Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
            cclMass= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Mass Centa-City Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
            cclHK = response.xpath('//*[@id="AutoNumber4"]//tr[2]/td[2]//text()').extract()[0]
            cclKln = response.xpath('//*[@id="AutoNumber4"]//tr[3]/td[2]//text()').extract()[0]
            cclNTE = response.xpath('//*[@id="AutoNumber4"]//tr[4]/td[2]//text()').extract()[0]
            cclNTW = response.xpath('//*[@id="AutoNumber4"]//tr[5]/td[2]//text()').extract()[0]
            print "-->",sdate,edate,ccl, cclLarge, cclSmallMedium, cclMass, cclHK, cclKln, cclNTE, cclNTW
            self.saveCCL(sdate,edate,ccl, cclLarge, cclSmallMedium, cclMass, cclHK, cclKln, cclNTE, cclNTW)

    ################################################################
    def saveCCL(self, sdate,edate, ccl, cclLarge, cclSmallMedium, cclMass, cclHK, cclKln, cclNTE, cclNTW):
        conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master' % (os.environ['STAGE']))
        cursor = conn.cursor()
        stmt = """REPLACE INTO Centa_CCL
        (FromDate, ToDate, CCL, CCL_L, CCL_SM, CCL_mass, CCL_HK, CCL_KLN, CCL_NTE, CCL_NTW)
        VALUES ('%s', '%s', %s , %s , %s , %s  , %s , %s , %s , %s )
        """ % (sdate.strftime('%Y-%m-%d'),edate.strftime('%Y-%m-%d'), ccl, cclLarge, cclSmallMedium, cclMass, cclHK, cclKln, cclNTE, cclNTW)
        print stmt
        try:
            r = cursor.execute(stmt)
        except Exception, e:
            print "EXCEPTION", e
            raise
        print "Done!"
        conn.commit()
        conn.close()