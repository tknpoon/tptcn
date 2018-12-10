#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import re,os, json, urllib,urllib2
import datetime as dt
import MySQLdb as my

################################

class hkabSpider(scrapy.Spider):
    name = 'hkab'

    urlToScrap = os.environ['URL_TO_SCRAP']
    start_urls = [urlToScrap]
    
    thedate = dt.datetime.strptime(os.path.basename(urlToScrap)[4:12], '%Y%m%d')
    
    ################################
    def parse(self, response):
        thelist= self.parseNow(response)
        return self.saveDay(thelist)
        
    ################################
    def parseNow(self, response):
        table=response.xpath('//*[contains(text(),"Rates as at")]/../../..')
        return [
        self.parseHeader(table, 'Rates as at'),
        self.parseRow(table, 'Overnight'),
        self.parseRow(table, '1 Week'),
        self.parseRow(table, '2 Weeks'),
        self.parseRow(table, '1 Month'),
        self.parseRow(table, '2 Months'),
        self.parseRow(table, '3 Months'),
        self.parseRow(table, '6 Months'),
        self.parseRow(table, '12 Months')
        ]
        
    ################################
    def parseRow(self, response, rowText):
        data=response.xpath('//*[contains(text(),"%s")]/..//td[2]/text()' % (rowText))
        if len(data) > 0:
            rate= data.extract()[0]
            try:
                float(rate)
                return rate
            except:
                pass
        return None

    ################################
    def parseHeader(self, response, rowText):
        data=response.xpath('//*[contains(text(),"%s")]//text()' % (rowText))
        if len(data) > 0:
            for d in data:
                try:
                    tdate = dt.datetime.strptime(d.extract().strip(), '%d/%m/%Y')
                    return tdate
                except:
                    pass
        return None

    ################################################################
    def saveDay(self, dlist):
        [tdate, von, v1w, v2w, v1m, v2m , v3m , v6m, v12m] = dlist
        print dlist
        
        conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master' % (os.environ['STAGE']))
        cursor = conn.cursor()
        
        #####
        stmts=[]
        stmts.append("REPLACE INTO `%s` ( `%s` ) VALUES ( '%s' );" % ('hkab', 'Date', tdate.strftime('%Y-%m-%d')))
        if von is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', 'Overnight', von, tdate.strftime('%Y-%m-%d')))
        if v1w is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '1W', v1w, tdate.strftime('%Y-%m-%d')))
        if v2w is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '2W', v2w, tdate.strftime('%Y-%m-%d')))
        if v1m is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '1M', v1m, tdate.strftime('%Y-%m-%d')))
        if v2m is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '2M', v2m, tdate.strftime('%Y-%m-%d')))
        if v3m is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '3M', v3m, tdate.strftime('%Y-%m-%d')))
        if v6m is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '6M', v6m, tdate.strftime('%Y-%m-%d')))
        if v12m is not None: stmts.append("UPDATE `%s` SET `%s`=%s WHERE `Date` ='%s';" % ('hkab', '12M', v12m, tdate.strftime('%Y-%m-%d')))
        for stmt in stmts:
            try:
                print stmt
                r= cursor.execute(stmt)
            except Exception, e:
                print "EXCEPTION", e
                raise
            conn.commit()
            print "done:" , stmt
            
        conn.close()
