#!/usr/bin/python
import zipfile, os, re, pymysql, glob
import datetime as dt

#################################
def parseDate(thelines):
    #,,,"Prev.BUSINESS DAY",,,,,,,,"BUSINESS DAY"
    #,,,"05 DEC 2018, WEDNESDAY",,,,,,,,"06 DEC 2018, THURSDAY ",,,,,,,,
    busDayMet=False
    for l in thelines:
        line = l.strip()
        #print line
        thelist=line.split(',')
        if busDayMet:
            m = re.findall(r'\d+\s+\w+\s+\d+', line)
            resultlist=[]
            for t in m:
                resultlist.append(dt.datetime.strptime(t, "%d %b %Y"))
            print resultlist
            return resultlist
        else:
            if 'BUSINESS DAY' in line:
                busDayMet = True
                #print line

#################################
def saveSalesNew(thedates, salesList):
    today = thedates[-1]
    if len(thedates) == 2:
        if thedates[0] > thedates[1]: today = thedates[0]
    todaystr=today.strftime('%Y-%m-%d')
    
    conn = pymysql.connect(host='g_mysql', db='%s_master'%(os.environ['STAGE']),
            user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'] )
    cursor = conn.cursor()
    
    print "Working on", todaystr
    
    stmts=[]
    for sales in salesList:
        sales = sales.replace('-,' , '0,')
        if sales[-1]=='-': sales=sales[:-1] + '0'
        
        #print sales
        if len(sales.split(',')) == 20:
            vContractMonth,vStrike,vCallPut,\
            vNiteOpen,vNiteHigh,vNiteLow,vNiteClose,vNiteVolume,\
            vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,vDayVolume,\
            vContractHigh,vContractLow,vVolume,\
            vOpenInt,vChangeOI = sales.split(',')
            vContractMonthStr=dt.datetime.strptime(vContractMonth,"%b-%y").strftime("%Y%m")
            
            stmts.append("""INSERT INTO `hhio_sales`
            (`Date`,`ContractMonth`,`Strike`,`CallPut`,
            `NiteOpen`,`NiteHigh`,`NiteLow`,`NiteClose`,`NiteVolume`,
            `DayOpen`,`DayHigh`,`DayLow`,`DayClose`,`ChangePrice`,`IV`,`DayVolume`,
            `ContractHigh`,`ContractLow`,`Volume`,
            `OpenInt`,`ChangeOI`
            )
            VALUES('%s','%s',%s,'%s', %s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s, %s,%s,%s, %s,%s )
            ON DUPLICATE KEY UPDATE
            `NiteOpen`=%s,`NiteHigh`=%s,`NiteLow`=%s,`NiteClose`=%s,`NiteVolume`=%s,
            `DayOpen`=%s,`DayHigh`=%s,`DayLow`=%s,`DayClose`=%s,`ChangePrice`=%s,`IV`=%s,`DayVolume`=%s,
            `ContractHigh`=%s,`ContractLow`=%s,`Volume`=%s,
            `OpenInt`=%s,`ChangeOI`=%s
            ;""" % (todaystr,vContractMonthStr,vStrike,vCallPut,\
                vNiteOpen,vNiteHigh,vNiteLow,vNiteClose,vNiteVolume,\
                vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,vDayVolume,\
                vContractHigh,vContractLow,vVolume,\
                vOpenInt,vChangeOI,\
                vNiteOpen,vNiteHigh,vNiteLow,vNiteClose,vNiteVolume,\
                vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,vDayVolume,\
                vContractHigh,vContractLow,vVolume,\
                vOpenInt,vChangeOI \
                )
            )
        elif len(sales.split(',')) == 12:
            vContractMonth,vStrike,vCallPut,\
            vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,\
            vVolume,\
            vOpenInt,vChangeOI = sales.split(',')

            vContractMonthStr=dt.datetime.strptime(vContractMonth,"%b-%y").strftime("%Y%m")
            
            stmts.append("""INSERT INTO `hhio_sales`
            (`Date`,`ContractMonth`,`Strike`,`CallPut`,
            `DayOpen`,`DayHigh`,`DayLow`,`DayClose`,`ChangePrice`,`IV`,
            `Volume`,
            `OpenInt`,`ChangeOI`
            )
            VALUES('%s','%s',%s,'%s', %s,%s,%s,%s,%s,%s, %s, %s,%s )
            ON DUPLICATE KEY UPDATE
            `DayOpen`=%s,`DayHigh`=%s,`DayLow`=%s,`DayClose`=%s,`ChangePrice`=%s,`IV`=%s,
            `Volume`=%s,
            `OpenInt`=%s,`ChangeOI`=%s
            ;""" % (todaystr,vContractMonthStr,vStrike,vCallPut,\
                vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,\
                vVolume,\
                vOpenInt,vChangeOI,\
                vDayOpen,vDayHigh,vDayLow,vDayClose,vChangePrice,vIV,\
                vVolume,\
                vOpenInt,vChangeOI
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
def parseSales(thedates, thelines):
    salesList=[]

    inBlock=False
    for l in thelines:
        line = l.strip()
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
    saveSalesNew(thedates, salesList)
    
#################################
def parseLines(thelines):
    thedates = parseDate(thelines)
    if thedates is not None:
        parseSales(thedates, thelines)

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
