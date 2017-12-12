REPLACE INTO tDailyPrice
(`vendorName`,`symbol`,`priceDate`,`openPrice`,`highPrice`,`lowPrice`,`closePrice`,`volume`,`adjClosePrice`)
SELECT 'yahoo'
, `symbol`
, `Date` as `priceDate`
, `Open` as `openPrice`
, GREATEST(`Open`, `Close`, `High`) as `highPrice`
,    LEAST(`Open`, `Close`, `Low` ) as `lowPrice`
, `Close` as `closePrice`
, `Volume` as `volume`
, `Adj Close` as `adjClosePrice`
FROM `tDailyPrice_yahoo`
