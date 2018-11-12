#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy, string
import re,os, json, urllib,urllib2
import datetime as dt

################################

class rtrSpider(scrapy.Spider):
    name = 'rtr'
    start_urls = [ os.environ['URL_TO_SCRAP'] ]
    
    ################################
    def parse(self, response):
        # //*[@id="topContent"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[18]/td[1]/a
        for row in range(2,18+1):
            col=1
            xp = '//*[@id="topContent"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[%d]/td[%d]//text()' %(row,col)
            for i in response.xpath(xp).extract():
                str = u''.join(i).encode('utf-8').strip()
                filtered_string = filter(lambda x: x in string.printable, str)
                mystr=' '.join(filtered_string.split())
                #for s in mystr:
                #    print '[',s,ord(s),']',
                print '[', mystr,  ']',
            print '+',
            
            for col in range(2,6+1):
                xp = '//*[@id="topContent"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[%d]/td[%d]//text()' %(row,col)
                for i in response.xpath(xp).extract():
                    print '[', u''.join(i).encode('utf-8').strip(), ']',
                print '+',
            print
        # xp = '//*[@id="topContent"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/a/@href'
