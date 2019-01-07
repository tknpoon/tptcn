#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

sql='
USE `p_master`;
SELECT 
`hkma`.`Date` AS `==hkmaDate` , `hkma`.`Count` AS `hkmaCount`  ,
`hkab`.`Date` AS `==hkabDate` , `hkab`.`Count` AS `hkabCount`  ,
`quot`.`Date` AS `==quoteDate`  , `quot`.`Count` AS `quotesCount`  , 
`sales`.`Date` AS `==salesDate`  , `sales`.`Count` AS `salesCount`  ,
`stkorpt`.`Date` AS `==stkoRdate`  , `stkorpt`.`Count` AS `stkoRcount`  , 
`stkosales`.`Date` AS `==stkoSdate`  , `stkosales`.`Count` AS `stkoScount`  ,
`hsio`.`Date` AS `==hsioDate`  , `hsio`.`Count` AS `hsioScount`  ,
`hhio`.`Date` AS `==hhioDate`  , `hhio`.`Count` AS `hhioScount`  ,
`ccl`.`ToDate` AS `==cclDate` , `ccl`.`CCL` AS `cclCCL`  
FROM
(SELECT `ToDate`,`CCL`  FROM `Centa_CCL` ORDER BY `ToDate` DESC LIMIT 0,1) AS `ccl`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkma_bal` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `hkma`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkab` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `hkab`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `stko_report` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `stkorpt`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `stko_sales` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `stkosales`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hsio_sales` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `hsio`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hhio_sales` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `hhio`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkex_quotation` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `quot`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkex_sales` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `sales`
;
SELECT "###";
SELECT MAX(`Date`) AS `today` FROM `consolidated_daily` ;
SELECT `symbol`,`Close`,`RSI`,`ATR_10`,`VWAP`,`VWAPam`,`VWAPpm` FROM `consolidated_daily` 
WHERE `symbol` IN (SELECT `symbol` FROM `diary` WHERE SUBSTRING(`radar`,-2,1)='1')
  AND `Date` >= (SELECT MAX(`Date`) FROM `consolidated_daily` )
ORDER BY `symbol`
;
'

echo $sql | docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --vertical | grep -v '^\*\*\*\*' | docker exec -i ${TAG_NAME:0:1}_telegram python /send_telegram.py

