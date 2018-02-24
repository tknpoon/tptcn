import scrapy
import re,os
import datetime as dt
import MySQLdb as my


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
        ##
        conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DATABASE'])
        cursor = conn.cursor()
        stmt = """REPLACE INTO tHKMA 
        (Date,
            CertIndebtAfterDisc, CertIndebtBeforeDisc,
            GovtCirAfterDisc, GovtCirBeforeDisc, 
            CloseAggBalAfterDisc, CloseAggBalBeforeDisc, 
            OutstandEFNAfterDisc, OutstandEFNBeforeDisc, 
            OutstandEFNBankAfterDisc, OutstandEFNBankBeforeDisc,
            Total)  
        VALUES ('%s',
            %d, %d,
            %d, %d,
            %d, %d,
            %d, %d,
            %d, %d,
            %d )
        """ % ( self.thedate.strftime('%Y-%m-%d'), 
            int(CertIndebtAfterDisc), int(CertIndebtBeforeDisc), 
            int(GovtCirAfterDisc), int(GovtCirBeforeDisc), 
            int(CloseAggBalAfterDisc), int(CloseAggBalBeforeDisc), 
            int(OutstandEFNAfterDisc), int(OutstandEFNBeforeDisc), 
            int(OutstandEFNBankAfterDisc), int(OutstandEFNBankBeforeDisc), 
            int(Total))
        try:
            r = cursor.execute(stmt)
        except Exception, e:
            print stmt
            raise
            
        conn.commit()
            
        conn.close()
    
