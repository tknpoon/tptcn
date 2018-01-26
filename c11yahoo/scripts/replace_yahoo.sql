REPLACE INTO tDailyPrice(`symbol`, `priceDate`, `openPrice`, `highPrice`, `lowPrice`, `closePrice`, `volume`, `adjClosePrice`)
  SELECT y.`symbol`, y.`Date` as `priceDate`,
    y.`Open` as `openPrice`, 
    GREATEST(y.`Open`, y.`Close`, y.`High`) as `highPrice`,
    LEAST(y.`Open`, y.`Close`, y.`Low` ) as `lowPrice`,
    y.`Close` as `closePrice`,
    y.`Volume` as `volume`,
    y.`Adj Close` as `adjClosePrice`
  FROM `tYAHOO_Daily` AS y
  WHERE y.`symbol` IN 
    (SELECT `tSymbol`.`symbol` FROM `tSymbol` WHERE `preferredVendor`='yahoo')
