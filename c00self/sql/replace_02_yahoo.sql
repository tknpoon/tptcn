USE secmaster;

REPLACE INTO tDailyPrice (symbol,date,open,high,low,close,volume)
SELECT 
    t2.symbol, 
    tYAHOO_Daily.Date as date,
    tYAHOO_Daily.Open as open,
    tYAHOO_Daily.High as high,
    tYAHOO_Daily.Low as low,
    tYAHOO_Daily.Close as close,
    tYAHOO_Daily.Volume as volume
FROM 
    tYAHOO_Daily,  
    (
    SELECT 
      symbol,
      code,
      IFNULL(Date,DATE(NOW())) AS startDate, 
      IFNULL(endDate,DATE(NOW())) AS endDate
    FROM tSymbolMeta
    WHERE type='source'
      AND vendor='yahoo'
    ) t2
WHERE tYAHOO_Daily.symbol = t2.code
  AND tYAHOO_Daily.Date >= t2.startDate
  AND tYAHOO_Daily.Date <= t2.endDate

