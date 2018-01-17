import scrapy
import re,os
import datetime as dt
import MySQLdb as my


class QuotSpider(scrapy.Spider):
    name = 'quot'
    urlToScrap = os.environ['URL_TO_SCRAP']
    #start_urls = [dt.datetime.today().strftime('http://web/raw/hkex_quot/%Y/d%y%m%de.htm')]
    start_urls = [urlToScrap]
    
    ################################
    def parse(self, response):
        wholequotes=[]
        for line in response.css("::text").extract():
            wholequotes.extend(line.replace("\r\n", "\n").splitlines())
        thedate = self.getDate(wholequotes)
        #print "thedate",thedate
        if thedate is None:
            return
        
        quotes = self.getQuotes(wholequotes)
        self.saveQuotes(thedate, quotes)
        
    ################################################################
    ################################################################
    def getDate(self, wholequotes):
        for q in wholequotes:
            mm = re.search('DATE: (\S+ \S+ \S+) ', q)
            if mm:
                return dt.datetime.strptime(mm.group(1),'%d %b %Y')
        return None
    
    ################################################################
    ################################################################
    def saveQuotes(self, thedate, quotes):
        ##
        conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
        cursor = conn.cursor()
        for row in quotes:
            stmt = """INSERT INTO tHKEX_Quotation (symbol, Date)  VALUES   ('%s',   '%s')
            ON DUPLICATE KEY UPDATE Currency='%s'
            """ % ( row['symbol'], thedate.strftime('%Y-%m-%d'), row['cur'] )
            r = cursor.execute(stmt)
            
            stmt = "UPDATE tHKEX_Quotation SET "
            stmt = stmt + " Currency='%s' " % (row['cur'])
            if 'pclose' in row: stmt = stmt + ", PrevClose=%f " %(row['pclose'])
            if 'high' in row:   stmt = stmt + ", High=%f " %(row['high'])
            if 'low' in row:    stmt = stmt + ", Low=%f " %(row['low'])
            if 'close' in row:  stmt = stmt + ", Close=%f " %(row['close'])
            if 'bid' in row:    stmt = stmt + ", Bid=%f " %(row['bid'])
            if 'ask' in row:    stmt = stmt + ", Ask=%f " %(row['ask'])
            if 'vol' in row:    stmt = stmt + ", Volume=%d " %(row['vol'])
            if 'tover' in row:  stmt = stmt + ", Turnover=%d " %(row['tover'])
            stmt = stmt + " WHERE symbol = '%s' and Date = '%s'" %(row['symbol'], thedate.strftime('%Y-%m-%d'))
            r = cursor.execute(stmt)
            conn.commit()
        conn.close()
    
    ################################################################
    def getQuotes(self, wholequotes):
        quotes=[]
        quoteList = self.getQuoteList(wholequotes)
        for q in quoteList:
            if len(q) < 148: continue
            #print q
            symbol = '{:04d}.HK'.format(int(q[0:6].replace('*','').strip()))
            name = q[7:24].strip()
            cur = q[24:27].strip()
            pclose = q[27:37].strip().replace(',', '')
            ask = q[37:45].strip().replace(',', '')
            high = q[45:54].strip().replace(',', '')
            vol = q[54:74].strip().replace(',', '')
            close = q[99:111].strip().replace(',', '')
            bid = q[111:119].strip().replace(',', '')
            low = q[119:128].strip().replace(',', '')
            tover = q[128:148].strip().replace(',', '')

            t={}
            t['symbol'] = symbol
            t['name'] = name
            t['cur'] = cur
            if (pclose <> '-' and pclose <> 'N/A'): t['pclose'] = float(pclose)
            if (high <> '-' and high <> 'N/A'):     t['high'] = float(high)
            if (low <> '-' and low <> 'N/A'):       t['low'] = float(low)
            if (close <> '-' and close <> 'N/A'):   t['close'] = float(close)
            if (bid <> '-' and bid <> 'N/A'):       t['bid'] = float(bid)
            if (ask <> '-' and ask <> 'N/A'):       t['ask'] = float(ask)
            if (vol <> '-' and vol <> 'N/A'):       t['vol'] = int(vol)
            if (tover <> '-' and tover<> 'N/A'):    t['tover'] = int(tover)

            quotes.append(t)
        return quotes
#        print "start"
#        for quote in quotes:
#            print quote
#        print "end"
            
        
    ################################################################
    def getQuoteList(self, wholequotes):
        quoteList=[]
        quote=""
        inQuote=False
        quotationLines=self.getQuotations(wholequotes)
        for quoteline in quotationLines:
            mm = re.match('^[\s\*]\s*\d+', quoteline[:6])
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
            #print toc_met, quotations_start, len(quotations) ,len(line), line
            if not toc_met and re.match('^\s*-+\s*$', line) is not None: 
                toc_met = True
                next
            if toc_met and not quotations_start and re.match('^\s*QUOTATIONS', line) is not None:
                quotations_start=True
            if toc_met and quotations_start:
                quotations.append(line)
                if re.match('^\s*-+\s*$', line): 
                    break
        return quotations
