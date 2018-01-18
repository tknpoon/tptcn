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
        
        sales = self.getSales(wholequotes)
        self.saveSales(thedate, sales)
        
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
    def saveSales(self, thedate, sales):
        ##
        conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
        cursor = conn.cursor()
        for row in sales:
            #{'symbol': '83199.HK', 'stockSales': [], 'name': u'CSOP 5YCGBOND-R'}^M
            for s in row['stockSales']:
                #'stockSales': [{'vol': u'3000', 'serial': 'M00001', 'price': u'24.80', 'flag': u'Y'}]
                stmt = """INSERT INTO 
                 tHKEX_Sales (symbol, Date, Serial, Flag, Price, Volume)  
                      VALUES ('%s',   '%s', '%s',   '%s', %f,    %d )
                  ON DUPLICATE KEY UPDATE Flag='%s'
                """ % ( row['symbol'], 
                thedate.strftime('%Y-%m-%d'), 
                s['serial'],
                s['flag'],
                float(s['price']),
                int(s['vol']),
                s['flag']
                )
                #print stmt
                r = cursor.execute(stmt)
            conn.commit()
            
        conn.close()
    
    ################################################################
    def getSales(self, wholequotes):
        sales=[]
        stockTradeLines = self.getStockTradeLine(wholequotes)
        #
        for line in stockTradeLines:
            stockDict={}
            # 83199 CSOP 5YCGBOND-R  < >[ ]/-//[ 1,000-101.75 ]< >
            mm = re.search('^\s*(\d+)\D(.+)\s*\<(.+)\>\s*\[(.+)\]/-//\s*\[(.+)\]\s*\<(.+)\>', line)
            if mm:
                stockDict['symbol'] = '{:04d}.HK'.format(int(mm.group(1).strip()))
                stockDict['name'] = mm.group(2).strip()
                
                stockSales=[]
                stockSales.extend(self.splitTrades('A', mm.group(3).strip()))
                stockSales.extend(self.splitTrades('M', mm.group(4).strip()))
                stockSales.extend(self.splitTrades('P', mm.group(5).strip()))
                stockSales.extend(self.splitTrades('U', mm.group(6).strip()))
                stockDict['stockSales'] = stockSales
                sales.append(stockDict)
                
        #for t in sales:
        #    print t
            
        return sales
        
    ################################################################
    def splitTrades(self, sess, tradeline):
        trades = []
        serial=1
        
        line = tradeline.strip()
        
        pattern='^([^\d\,\.]*)([,\.\d]+)-([,\.\d]+)\s+(.*)$'
        m = re.search(pattern, line)
        while (m):
            #print line
            d = {}
            d['serial'] = "%s%05d" % (sess, serial)
            d['flag'] = m.group(1).strip() if m.group(1) else ""
            d['vol'] = m.group(2).replace(',', '')
            d['price'] = m.group(3).replace(',', '')
            #print d
            trades.append(d)
            #
            serial = serial + 1
            line = m.group(4).strip() if m.group(4) else ""
            m = re.search(pattern, line)
            
        return trades
        
    ################################################################
    def getStockTradeLine(self, wholequotes):
        tradeList=[]
        trade=""
        inTrade=False
        tradeLines=self.getTradelines(wholequotes)
        for line in tradeLines:
            mm = re.match('^\s*\d+', line[:5])
            #print "@@", inTrade, line, mm
            if mm :
                if inTrade: 
                    #print "mi", trade
                    tradeList.append(trade)
                    trade = line
                    inTrade = True
                else:
                    trade = line
                    #print "mn", trade
                    inTrade = True
            else:
                if inTrade:
                    trade = trade + line
                    #print "ni", trade
                #else:
                    #print "nn", trade
                
        return tradeList
        
    ################################################################
    def getTradelines(self, wholequotes):
        trades=[]
        toc_met=False
        trades_start1=False
        trades_start2=False
        for line in wholequotes:
            #print toc_met, trades_start, len(trades) ,len(line), line
            if not toc_met and re.match('^\s*-+\s*$', line) is not None: 
                toc_met = True
                next
            if toc_met and not trades_start1 and re.match('^\s*SALES RECORDS FOR ALL STOCKS', line) is not None:
                trades_start1=True
            if toc_met and trades_start1 and not trades_start2 and re.match('^\s*CODE  NAME OF STOCK    SALES RECORD', line) is not None:
                trades_start2=True
            if toc_met and trades_start1 and trades_start2:
                if re.match('^\s*-+\s*$', line): 
                    break
                else:
                    trades.append(line)
        return trades

    ################################################################
    ################################################################
    def saveQuotes(self, thedate, quotes):
        ##
        conn = my.connect(host='db', user=os.environ['MYSQL_USER'],passwd=os.environ['MYSQL_PASSWORD'],db=os.environ['MYSQL_DB'])
        cursor = conn.cursor()
        for row in quotes:
            stmt = """INSERT INTO tHKEX_Quotation (symbol, Date, Name)  VALUES   ("%s", "%s", "%s")
            ON DUPLICATE KEY UPDATE Name="%s"
            """ % ( row['symbol'], thedate.strftime('%Y-%m-%d'), row['name'] , row['name'] )
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
