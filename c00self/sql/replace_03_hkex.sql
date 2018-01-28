USE secmaster;

REPLACE INTO tDailyPrice (symbol,date,open,high,low,close,volume)
    SELECT 
        t2.symbol, 
        q.Date as date,
        IF(q.PrevClose > q.High, q.High, IF(q.PrevClose < q.Low, q.Low, q.PrevClose)) as open,
        q.High as high,
        q.Low as low,
        q.Close as close,
        q.Volume as volume
    FROM 
      tHKEX_Quotation q,
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
    WHERE 1
      AND q.symbol = t2.code
      AND q.Date >= t2.startDate
      AND q.Date <= t2.endDate

