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
        CertIndebtAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        self.saveDay(
            [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]
        )
        
    ################################################################
    def saveDay(self, dlist):
        [CertIndebtAfterDisc, CertIndebtBeforeDisc,
        GovtCirAfterDisc, GovtCirBeforeDisc, 
        CloseAggBalAfterDisc, CloseAggBalBeforeDisc, 
        OutstandEFNAfterDisc, OutstandEFNBeforeDisc, 
        OutstandEFNBankAfterDisc, OutstandEFNBankBeforeDisc,
        Total
        ] = dlist

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
    
