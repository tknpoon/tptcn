#!/usr/bin/python
import zipfile, os, re, pymysql, glob
import datetime as dt

#################################
def parseDate(thelines):
    #"STOCK OPTIONS DAILY MARKET REPORT AS AT 21 DEC 2018"
    for line in thelines:
        m = re.match('^\"STOCK OPTIONS DAILY MARKET REPORT AS AT (.*)\"', line)
        if m :
            return dt.datetime.strptime(m.group(1), "%d %b %Y")

#################################
def saveReport(thedate, slines):
        conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
                user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
        cursor = conn.cursor()
        
        stmts=[]
        for s in slines:
            #print s
            s = s.replace(',-,', ',0,')
            if s[-1:]=='-': s=s[:-1] + '0'

            code,name,id,totalVol,callVol,putVol,totalOI,callOI,putOI,IV = s.split(',')
            realid = id.replace("(","").replace(")","").replace(" ","")
            stmts.append("""INSERT INTO `stko_report`
                ( `Date`,`Code`,`BaseStockName`,`BaseSymbol`,`TotalVol`,`CallVol`,`PutVol`,`TotalOI`,`CallOI`,`PutOI`,`IV`)
                VALUES("%s","%s","%s",           "%s",       %s,        %s,        %s,      %s,      %s,        %s,    %s )
                ON DUPLICATE KEY UPDATE
                `BaseStockName`="%s",
                `BaseSymbol`="%s",
                `TotalVol`=%s,
                `CallVol`=%s,
                `PutVol`=%s,
                `TotalOI`=%s,
                `CallOI`=%s,
                `PutOI`=%s,
                `IV`=%s
                ;""" % 
                (thedate.strftime('%Y-%m-%d'), code, name, realid, totalVol,callVol,putVol,totalOI,callOI,putOI,IV 
                                                    ,name, realid, totalVol,callVol,putVol,totalOI,callOI,putOI,IV 
                )
            )
        for stmt in stmts:
            try:
                #print stmt
                r= cursor.execute(stmt)
            except Exception, e:
                print "EXCEPTION", e
                print stmt
                raise
        conn.commit()
        conn.close()
        return    
    
#################################
def parseReport(thedate, thelines):
    slines=[]
    sTitleMet=False
    for l in thelines:
        line = l.strip()
        #if line == ',,,"SUMMARY TRADING VOLUME",,,"SUMMARY OPEN INTEREST"': 
        if line == '"HKATS CODE","UNDERLYING STOCK",,"TOTAL","CALLS","PUTS","TOTAL","CALLS","PUTS","IV%*"':
            sTitleMet=True
            continue
        ##
        if sTitleMet :
            if len(line.strip()) > 0:
                slines.append(line)
            else:
                break
    saveReport(thedate, slines)

#################################
def savePrice(thedate, priceDict):
        conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
                user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
        cursor = conn.cursor()
        
        stmts=[]
        for code in priceDict.keys():
            stmts.append("""UPDATE `stko_report` SET `StockClose`=%s
                WHERE `Date` = '%s' AND `Code` = '%s'
                ;""" % (priceDict[code], thedate.strftime('%Y-%m-%d'), code)
            )
        for stmt in stmts:
            try:
                #print stmt
                r= cursor.execute(stmt)
            except Exception, e:
                print "EXCEPTION", e
                print stmt
                raise
        conn.commit()
        conn.close()
        return    

#################################
def saveSales(thedate, salesList):
        datestr=thedate.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
                user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
        cursor = conn.cursor()
        ###
        stmts=[]
        for sales in salesList:
            #print sales,
            sales = sales.replace(',-,', ',0,')
            if sales[-1:]=='-': sales=sales[:-1] + '0'
            #print sales
            code,mth,strike,cp,open,high,low,settle,changeSettle,iv,volume,oi,changeOi = sales.split(',')
            mthstr=dt.datetime.strptime(mth,"%b%y").strftime("%Y%m")
            
            stmts.append("""INSERT INTO `stko_sales`
            (`Date`,`Code`,`ContractMonth`,`Strike`,`CallPut`,`Open`,`High`,`Low`,`Settlement`,`ChangeSettlement`,`IV`,`Volume`,`OpenInt`,`ChangeOI`)
            VALUES('%s','%s','%s',%s,'%s' ,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
            `Open`=%s,
            `High`=%s,
            `Low`=%s,
            `Settlement`=%s,
            `ChangeSettlement`=%s,
            `IV`=%s,
            `Volume`=%s,
            `OpenInt`=%s,
            `ChangeOI`=%s
                ;""" % (datestr,code,mthstr,strike,cp,open,high,low,settle,changeSettle,iv,volume,oi,changeOi
                                                     ,open,high,low,settle,changeSettle,iv,volume,oi,changeOi)
            )
            
        for stmt in stmts:
            try:
                #print stmt
                r= cursor.execute(stmt)
            except Exception, e:
                print "EXCEPTION", e
                print stmt
                raise
        conn.commit()
        conn.close()
        return    

#################################
def parseSales(thedate, thelines):
    salesList=[]
    priceDict={}
    
    code = None
    price = None
    for l in thelines:
        line = l.strip()
        #print line
        m = re.match('^\"CLASS (\S+)\s+\-\s+[^\"]+\",,,\"CLOSING PRICE HK\$\s+([\d\.]+)\"', line)
        if m:
            code = m.group(1)
            price = m.group(2)
        m = re.match('^\"CLASS\",', line)
        if m:
            code = None
            price = None
        if code is not None and price is not None and len(line)>0 and line[0] <> '"' and line[0] <> ',':
            priceDict[code]=price
            salesList.append ( "%s,%s" %(code,line) )
    
    savePrice(thedate, priceDict)
    saveSales(thedate, salesList)
    
#################################
def parseLines(thelines):
    thedate = parseDate(thelines)
    parseReport(thedate, thelines)
    parseSales(thedate, thelines)

#################################
## main
#for f in glob.glob('/tmp/p/*.csv'):
#    lines=[]
#    with open(f, "r+") as myfile:
#        lines = myfile.readlines()
#    parseLines(lines)

with zipfile.ZipFile('/tmp/entrypoint.zip') as myzip:
    names = myzip.namelist()
    for name in names:
        print "Handling %s from %s" % (name, '/tmp/entrypoint.zip')
        lines=[]
        with myzip.open(name) as myfile:
            lines = myfile.readlines()
        parseLines(lines)
