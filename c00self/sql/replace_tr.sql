USE secmaster;

REPLACE INTO tDailyPrice (symbol,date,open,high,low,close,volume)
SELECT 
    t2.symbol, 
    tTR_Daily.Date as date,
    tTR_Daily.Open as open,
    tTR_Daily.High as high,
    tTR_Daily.Low as low,
    tTR_Daily.Close as close,
    tTR_Daily.Volume as volume
FROM 
    tTR_Daily,  
    (
    SELECT 
      symbol,
      code,
      IFNULL(Date,DATE(NOW())) AS startDate, 
      IFNULL(endDate,DATE(NOW())) AS endDate
    FROM tSymbolMeta
    WHERE type='source'
      AND vendor='tr'
    ) t2
WHERE tTR_Daily.symbol = t2.code
  AND tTR_Daily.Date >= t2.startDate
  AND tTR_Daily.Date <= t2.endDate

