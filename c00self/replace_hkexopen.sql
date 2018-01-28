USE secmaster;

UPDATE tDailyPrice (open)
SELECT 
    t2.symbol, 
    tHKEX_Sales.Date as date,
    tHKEX_Sales.PrevClose as open,
    tHKEX_Sales.High as high,
    tHKEX_Sales.Low as low,
    tHKEX_Sales.Close as close,
    tHKEX_Sales.Volume as volume
FROM 
    tHKEX_Sales,  
    (
    SELECT 
      symbol,
      code,
      IFNULL(Date,DATE(NOW())) AS startDate, 
      IFNULL(endDate,DATE(NOW())) AS endDate
    FROM tSymbolMeta
    WHERE type='source'
      AND vendor='hkex'
    ) t2
WHERE tHKEX_Sales.symbol = t2.code
  AND tHKEX_Sales.Date >= t2.startDate
  AND tHKEX_Sales.Date <= t2.endDate

