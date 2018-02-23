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
        #if self.thedate >= dt.datetime(2000,1,1) and self.thedate < dt.datetime(2012,5,16):
#        if self.thedate == dt.datetime(2011,10,20):
#            thelist= self.parse2011Z(response)
#        elif self.thedate == dt.datetime(2011,7,15):
#            thelist= self.parse2011X(response)
#        elif self.thedate >= dt.datetime(2000,8,1) and self.thedate < dt.datetime(2011,8,1):
#            thelist= self.parse2011W(response)
#        elif self.thedate >= dt.datetime(2011,8,1) and self.thedate < dt.datetime(2011,9,30):
#            thelist= self.parse2011X(response)
#        elif self.thedate >= dt.datetime(2011,9,30) and self.thedate < dt.datetime(2011,10,19):
#            thelist= self.parse2011Z(response)
#        elif self.thedate >= dt.datetime(2011,10,19) and self.thedate < dt.datetime(2011,10,31):
#            thelist= self.parse2011Y(response)
#        elif self.thedate >= dt.datetime(2011,10,31) and self.thedate < dt.datetime(2012,1,1):
#            thelist= self.parse2011Z(response)
#        elif self.thedate >= dt.datetime(2012,1,1) and self.thedate < dt.datetime(2012,10,31):
#            thelist= self.parse2012Y(response)
#        elif self.thedate >= dt.datetime(2012,10,31) and self.thedate < dt.datetime(2012,12,11):
#            thelist= self.parse2012Z(response)
#        elif self.thedate >= dt.datetime(2012,12,11) and self.thedate < dt.datetime(2013,6,26):
#            thelist= self.parse2013X(response)
#        elif self.thedate >= dt.datetime(2013,6,26) and self.thedate < dt.datetime(2013,6,28):
#            thelist= self.parse2013Y(response)
#        elif self.thedate >= dt.datetime(2013,6,28) and self.thedate < dt.datetime(2013,7,4):
#            thelist= self.parse2013Z(response)
#        else: ## self.thedate >= dt.datetime(2013,7,1):
#            thelist= self.parseLatest(response)
#            
        if self.thedate >= dt.datetime(2013,7,1):
            thelist= self.parseNow(response)

            
        #return self.saveDay(thelist)
    ################################
    def parseNow(self, response):
    # CERTIFICATES OF INDEBTEDNESS
        print "====="
        print response.xpath('//*[@id="content"]//td[contains(text(),"Total")]/ancestor::table//tr[7]').extract()
        print "====="

        return []

    ################################
    def parse2011W(self, response):
        print "parse2011W"
        print response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]//table/tbody/tr[2]/td[2]//font//text()[1]').extract()
                              #//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/center/table/tbody/tr[2]/td[2]/p/b/font/text()[1]
        CertIndebtAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]//table/tbody/tr[2]/td[2]//font/text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=re.sub('\([^\)]+\)','',''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn',''))
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]
    ################################
    def parse2011X(self, response):
        print "parse2011X"
        CertIndebtAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=re.sub('\([^\)]+\)','',''.join(response.xpath('//*[@id="content"]/div/table/tbody//tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]//span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn',''))
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]
    ################################
    def parse2011Y(self, response):
        print "parse2011Y"
        CertIndebtAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=re.sub('\([^\)]+\)','',''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td/span//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn',''))
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]
    ################################
    def parse2011Z(self, response):
        print "parse2011Z"
        CertIndebtAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p//strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p//strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p//strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p//strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]
    ################################
    def parse2012Y(self, response):
        print "parse2012Y"
        CertIndebtAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=''.join(response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p/strong//text()').extract()[:-1]).replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

    ################################
    def parse2012Z(self, response):
        print "parse2012Z"
        CertIndebtAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong//span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p/span/strong/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/span//strong/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p/span/strong/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

    ################################
    def parse2013X(self, response):
        print "parse2013X"
        CertIndebtAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

    ################################
    def parse2013Y(self, response):
        print "parse2013Y"
        CertIndebtAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong/span/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

    ################################
    def parse2013Z(self, response):
        print "parse2013Z"
        CertIndebtAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CertIndebtBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[2]/td[3]/p/strong/span/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirAfterDisc    =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        GovtCirBeforeDisc   =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[3]/td[3]/p/strong/span/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalAfterDisc =response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[2]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        CloseAggBalBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[4]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[2]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankAfterDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[5]/td[3]/p/strong/span[1]/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        OutstandEFNBankBeforeDisc=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[6]/td[3]/p/strong/span/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        Total=response.xpath('//*[@id="content"]/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr[7]/td[3]/p/strong/span/text()[1]').extract()[0].replace('\r','').replace('\n','').replace(' ','').replace(',','').replace('mn','')
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

    ################################
    def parseLatest(self, response):
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
        
        return [CertIndebtAfterDisc,
            CertIndebtBeforeDisc,
            GovtCirAfterDisc,
            GovtCirBeforeDisc,
            CloseAggBalAfterDisc,
            CloseAggBalBeforeDisc,
            OutstandEFNAfterDisc,
            OutstandEFNBeforeDisc,
            OutstandEFNBankAfterDisc,
            OutstandEFNBankBeforeDisc,Total]

        
    ################################################################
    def saveDay(self, dlist):
        [CertIndebtAfterDisc, CertIndebtBeforeDisc,
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
    
