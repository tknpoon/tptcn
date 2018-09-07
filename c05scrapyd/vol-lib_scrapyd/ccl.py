import scrapy
import re,os
import datetime as dt
import MySQLdb as my


class centaSpider(scrapy.Spider):
    name = 'centa'
    urlToScrap = os.environ['URL_TO_SCRAP']
    #start_urls = [dt.datetime.today().strftime('http://web/raw/hkex_quot/%Y/d%y%m%de.htm')]
    start_urls = [urlToScrap]
    
    ################################
    def parse(self, response):
		dateSent= response.xpath('//b[text()[contains(.,"Centa-City Leading Index CCL")]]/../..//text()').extract()[5]
		date_search = re.search('residential property price from (\S+) to', dateSent, re.IGNORECASE)
		if date_search:
			ddate = dt.datetime.strptime(date_search.group(1), '%Y/%m/%d')
			ccl= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
			cclLarge= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City (large units) Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
			cclSmallMedium= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Centa-City (small/medium units) Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
			cclMass= response.xpath('//*[@id="AutoNumber1"]//td//b[text()[contains(.,"[Mass Centa-City Leading Index]")]]/../../../td[2]//p/text()').extract()[0]
			print ccl, cclLarge, cclSmallMedium, cclMass
			self.saveCCL(ddate,ccl, cclLarge, cclSmallMedium, cclMass)
        
    ################################################################
    def saveCCL(self, ddate,ccl, cclLarge, cclSmallMedium, cclMass):
        conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DATABASE'])
        cursor = conn.cursor()
        stmt = """REPLACE INTO tCenta
        (Date, CCL, CCL_Large, CCL_SmallMedium, CCL_Mass)
        VALUES ('%s', %s , %s , %s , %s )
        """ % ( ddate.strftime('%Y-%m-%d'), ccl, cclLarge, cclSmallMedium, cclMass)
        try:
            r = cursor.execute(stmt)
        except Exception, e:
            print stmt
            raise
            
        conn.commit()
            
        conn.close()