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
        quotes = self.getQuotes(wholequotes)
        
    ################################################################
    ################################################################
    def getQuotes(self, wholequotes):
        quotes=[]
        quoteList = self.getQuoteList(wholequotes)
        for q in quoteList:
            if len(q) < 148: continue
            symbol = '{:04d}.HK'.format(int(q[1:6].strip()))
            name = q[7:24].strip()
            cur = q[24:27].strip()
            pclose = float(q[27:37].strip().replace(',', ''))
            ask = float(q[37:45].strip().replace(',', ''))
            high = float(q[45:54].strip().replace(',', ''))
            vol = int(q[54:74].strip().replace(',', ''))
            close = float(q[99:111].strip().replace(',', ''))
            bid = float(q[111:118].strip().replace(',', ''))
            low = float(q[118:128].strip().replace(',', ''))
            turnover = float(q[128:148].strip().replace(',', ''))

            t={
                'symbol' : symbol,
                'name' : name,
                'cur' : cur,
                'pclose' : float( '-1' if pclose =='-' else pclose),
                'ask' : float( '-1' if ask =='-' else ask),
                'high' : float( '-1' if high =='-' else high),
                'vol' : int( '-1' if vol =='-' else vol),
                'close' : float( '-1' if close =='-' else close),
                'bid' : float( '-1' if bid =='-' else bid),
                'low' : float( '-1' if low =='-' else low),
                'turnover' : float( '-1' if turnover =='-' else turnover)
            }
            print t
            quotes.append(t)
        print "start"
        for quote in quotes:
            print quote
        print "end"
            
            
        
    ################################################################
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
        
    ################################################################
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