USE secmaster;

#UPDATE tDailyPrice1 dest,
#(

  SELECT 
    topen.symbol, 
    topen.Date as date,
    topen.Price as open
  FROM 
    (
        SELECT s1.symbol, s1.date, s1.Price
        FROM
          tHKEX_Sales s1
          JOIN (SELECT symbol, Date, MIN(Serial) as Serial
                FROM tHKEX_Sales
                WHERE tHKEX_Sales.Flag NOT IN ('P','M','D','C')
                GROUP BY symbol, Date
          ) s2
        ON s1.symbol = s2.symbol
         AND s1.Date = s2.Date
         AND s1.Serial = s2.Serial
    ) topen,
    (
      SELECT 
        symbol,
        code,
        IFNULL(Date,DATE(NOW())) AS startDate, 
        IFNULL(endDate,DATE(NOW())) AS endDate
      FROM tSymbolMeta
      WHERE type='source'
        AND vendor='hkex'
    ) tmeta
  WHERE topen.symbol = tmeta.code
    AND topen.date >= tmeta.startDate
    AND topen.date <= tmeta.endDate

#) src
