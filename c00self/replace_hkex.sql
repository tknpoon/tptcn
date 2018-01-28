USE secmaster;

REPLACE INTO tDailyPrice1 (symbol,date,open,high,low,close,volume)
SELECT 
    t2.symbol, 
    tHKEX_Quotation.Date as date,
    tHKEX_Quotation.PrevClose as open,
    tHKEX_Quotation.High as high,
    tHKEX_Quotation.Low as low,
    tHKEX_Quotation.Close as close,
    tHKEX_Quotation.Volume as volume
FROM 
    tHKEX_Quotation,  
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
WHERE tHKEX_Quotation.symbol = t2.code
  AND tHKEX_Quotation.Date >= t2.startDate
  AND tHKEX_Quotation.Date <= t2.endDate

