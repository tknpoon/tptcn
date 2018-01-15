import scrapy
import re

class QuotSpider(scrapy.Spider):
    name = 'quot'
    start_urls = ['http://web/raw/hkex_quot/2018/d180105e.htm']

    ################################
    def parse(self, response):
        wholequotes=[]
        for line in response.css("::text").extract():
            wholequotes.extend(line.replace("\r\n", "\n").splitlines())
        quoteList = self.getQuoteList(wholequotes)
        
        print "start"
        for q in quoteList:
            print q
        print "end"
    ################################
    def getQuoteList(self, wholequotes):
        quoteList=[]
        quote=""
        inQuote=False
        quotationLines=self.getQuotations(wholequotes)
        for quoteline in quotationLines:
            mm = re.match('^[\s\*]\s*\d+ ', quoteline)
            #print "@@", inQuote, quoteline, mm
            if mm :
                if inQuote: 
                    #print "mi", quote
                    quoteList.append(quote)
                    quote = quoteline
                    inQuote = True
                else:
                    quote = quoteline
                    #print "mn", quote
                    inQuote = True
            else:
                if inQuote:
                    quote = quote + quoteline
                    #print "ni", quote
                #else:
                    #print "nn", quote
                
        return quoteList
        
    ################################
    def getQuotations(self, wholequotes):
        quotations=[]
        toc_met=False
        quotations_start=False
        for line in wholequotes:
            #print toc_met, quotations_start, len(quotations) ,line
            if not toc_met and re.match('^\s*-+\s*$', line) is not None: 
                toc_met = True
                next
            if toc_met and not quotations_start and re.match('^QUOTATIONS', line) is not None:
                quotations_start=True
            if toc_met and quotations_start:
                quotations.append(line)
                if re.match('^\s*-+\s*$', line): 
                    break
        return quotations
