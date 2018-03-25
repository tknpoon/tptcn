REPLACE INTO tDailyPrice(`symbol`, `date`, `open`, `high`, `low`, `close`, `volume`, `adjClose`)
  SELECT y.`symbol`, y.`Date` as `date`,
    y.`Open` as `open`, 
    GREATEST(y.`Open`, y.`Close`, y.`High`) as `high`,
    LEAST(y.`Open`, y.`Close`, y.`Low` ) as `low`,
    y.`Close` as `close`,
    y.`Volume` as `volume`,
    y.`Adj Close` as `adjClose`
  FROM `tYAHOO_Daily` AS y
  WHERE 
    WEEKDAY(`tYAHOO_Daily`.`Date`) < 6
   AND 
    y.`symbol` IN 
    (SELECT `tSymbol`.`symbol` FROM `tSymbol` WHERE `preferredVendor`='yahoo')
