# -*- coding: utf-8 -*-
import scrapy
import re,os
import datetime as dt

class centaSpider(scrapy.Spider):
    name = 'cclhistory'
    urlToScrap = os.environ['URL_TO_SCRAP']
    start_urls = [urlToScrap]

    download_delay = 1.5
    
    ffdata ={ ## R1: v2  CCL=v2 / CCLlarge=v8 / CCLsmallMid=v9 / CCLmass=v4 / CCL district =v5
        'CCL_HK':   {'R1': 'v5', 'DropDownList3' : u"港島"},
        'CCL_KLN':  {'R1': 'v5', 'DropDownList3' : u"九龍" },
        'CCL_NTE':  {'R1': 'v5', 'DropDownList3' : u"新界(東)" },
        'CCL_NTW':  {'R1': 'v5', 'DropDownList3' : u"新界(西)" },
        'CCL_mass': {'R1': 'v4'},
        'CCL_L':    {'R1': 'v8'},
        'CCL_SM':   {'R1': 'v9'},
        'CCL':      {'R1': 'v2'}
    }
    
    ################################
    def parse(self, response):
        #tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        # //*[@id="AutoNumber1"]/tbody/tr
        tbl = response.xpath('//*[@id="AutoNumber1"]').extract()
        if len(tbl) > 0:
            print tbl
        else:
            #for c in self.ffdata:
            for c in ['CCL_mass', 'CCL']:
                iformdata = self.ffdata[c].copy()
                iformdata.update( { 'TextBox1' : '1990', 'DropDownList1' : '1', 'TextBox2' : '1'} )
                iformdata.update( { 'TextBox3' : '2019', 'DropDownList2' : '1', 'TextBox4' : '1'} )
                yield scrapy.FormRequest.from_response(
                    response,
                    formdata=iformdata,
                    callback=self.parsedata,
                    meta={'ccltype': c}
                )
                
    ################################
    def parsedata(self, response):
        trs = response.xpath('//*[@id="AutoNumber1"]//tr') #.extract()
        print len(trs)
        for tr in trs :  #skip the header
            try:
                tds = tr.xpath('td/text()')
                [fromstr, tostr] = tds[0].extract().split('-')
                fromdate = dt.datetime.strptime(fromstr.strip(), "%Y/%m/%d")
                todate =   dt.datetime.strptime(tostr.strip(),   "%Y/%m/%d")
                ccl_index = tds[1].extract()
                print response.meta['ccltype'], fromdate, todate, ccl_index
            except:
                pass
        print "END"
