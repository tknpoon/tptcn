#!/usr/bin/python
import zipfile, os, re, pymysql, glob
import datetime as dt

#################################
def parseDate(thelines):
    #,,,"BUSINESS DAY"
    #,,,"31 JUL 2014, THURSDAY "
    busDayMet=False
    for l in thelines:
        line = l.strip()
        thelist=line.split(',')
        if busDayMet:
            m = re.match('\"(\d+\s+\w+\s+\d+)', thelist[-2])
            if m:
                return dt.datetime.strptime(m.group(1), "%d %b %Y")
            break
        else:
            if thelist[-1] == '"BUSINESS DAY"':
                print line
                busDayMet = True

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
            print sales
            mth,strike,cp,open,high,low,settle,changeSettle,iv,volume,oi,changeOi = sales.split(',')
            mthstr=dt.datetime.strptime(mth,"%b-%y").strftime("%Y%m")
            
            stmts.append("""INSERT INTO `hsio_sales`
            (`Date`,`ContractMonth`,`Strike`,`CallPut`,`Open`,`High`,`Low`,`Settlement`,`ChangeSettlement`,`IV`,`Volume`,`OpenInt`,`ChangeOI`)
            VALUES('%s','%s',%s,'%s' ,%s,%s,%s,%s,%s,%s,%s,%s,%s)
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
                ;""" % (datestr,mthstr,strike,cp,open,high,low,settle,changeSettle,iv,volume,oi,changeOi
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

    inBlock=False
    for l in thelines:
        line = l.strip()
        #print line
        #"CONTRACT MONTH","STRIKE PRICE","C/P","*OPENING PRICE","*DAILY HIGH","*DAILY LOW","O.Q.P. CLOSE","O.Q.P. CHANGE","IV%","VOLUME","OPEN INTEREST","CHANGE IN OI"
        if not inBlock:
            m = re.match('^\"CONTRACT MONTH\",', line)
            if m:
                inBlock=True
        else:
            if len(line)>0: 
                salesList.append(line) 
            else:
                inBlock=False
    
    saveSales(thedate, salesList)
    
#################################
def parseLines(thelines):
    thedate = parseDate(thelines)
    print thedate
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
