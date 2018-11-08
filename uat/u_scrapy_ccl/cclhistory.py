#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import re,os
import datetime as dt
import urllib, urllib2, json

from scrapy.exceptions import DropItem

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
    
    ########################
    # valuedict : {fld : value, fld, value, ...}
    ##############################
    def save_sql(self, table, valuedict):
        ##
        conn = my.connect(host='g_mysql', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db='%s_master'%(os.environ['STAGE']))
        cursor = conn.cursor()
        #INSERT INTO t1 (a,b,c) VALUES (1,2,3)  ON DUPLICATE KEY UPDATE c=c+1;
        #print index,row
        stmt = "INSERT INTO %s (" %(table)
        for k in valuedict.keys():
            stmt = stmt + "`%s`," % ( valuedict[k])
        stmt = stmt[-1:] + ") "
        
        stmt = stmt + " VALUES("
        for k in valuedict.keys():
            stmt = stmt + "%s," % ( valuedict[k] )
        stmt = stmt[-1:] + ") "
        
        stmt = stmt + "ON DUPLICATE KEY UPDATE "
        for k in valuedict.keys():
            if k == 'FromDate': next
            stmt = stmt + "`%s`," % ( valuedict[k] )
        stmt = stmt[-1:] 

        print stmt
        #r = cursor.execute(stmt)
        #print "Exec result:",r
        
        conn.commit()
        conn.close()

    ################################
    def parse(self, response):
        #tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        # //*[@id="AutoNumber1"]/tbody/tr
        tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        if len(tbl) > 0:
            print tbl
        else:
            if True: #True means weekly jobs
                #for c in ['CCL','CCL_HK','CCL_KLN','CCL_NTE','CCL_NTW','CCL_L','CCL_SM','CCL_mass']:
                for c in ['CCL']:
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
                for c in ['CCL','CCL_HK','CCL_KLN','CCL_NTE','CCL_NTW','CCL_L','CCL_SM','CCL_mass']:
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
            tds = tr.xpath('td/text()')
            print tds[0].extract()
            [fromstr, tostr] = tds[0].extract().split('-')
            #
            rowdict = {
                'FromDate':dt.datetime.strptime(fromstr.strip(), "%Y/%m/%d").strftime("%Y-%m-%d"),
                'ToDate':dt.datetime.strptime(tostr.strip(),   "%Y/%m/%d").strftime("%Y-%m-%d"),
                response.meta['ccltype'] : tds[1].extract(),
                }
            print rowdict
            self.save_sql('Centa_CCL' , rowdict)
        print "END"
