import scrapy
import re,os
import datetime as dt
import MySQLdb as my

#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/span/text()
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/span/text()
#
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/span/text()
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/span/text()
#
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/span/text()
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/span/text()
#
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/span/text()
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/span/text()
#
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/span/text()
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/span/text()
#
#//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[2]/span/text()
#

class hkmaSpider(scrapy.Spider):
    name = 'quot'
    urlToScrap = os.environ['URL_TO_SCRAP']
    #start_urls = [dt.datetime.today().strftime('http://web/raw/hkma/%Y/moneybase%Y%m%d-2.html')]
    start_urls = [urlToScrap]
    
    ################################
    def parse(self, response):
        a=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        b=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        c=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        d=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        e=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        f=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        g=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        h=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        i=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        j=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        k=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','')
        print a,b,c,d,e,f,g,h,i,j,k

