#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

sql='
USE `p_master`;
SELECT 
`hkma`.`Date` AS `hkmaDate` , `hkma`.`Count` AS `hkmaCount`  ,
`quot`.`Date` AS `quoteDate`  , `quot`.`Count` AS `quotesCount`  , 
`sales`.`Date` AS `salesDate`  , `sales`.`Count` AS `salesCount`  ,
`ccl`.`ToDate` AS `cclDate` , `ccl`.`CCL` AS `cclCCL`  
FROM
(SELECT `ToDate`,`CCL`  FROM `Centa_CCL` ORDER BY `ToDate` DESC LIMIT 0,1) AS `ccl`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkma_bal` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `hkma`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkex_quotation` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `quot`,
(SELECT `Date`,COUNT(*) AS `Count` FROM `hkex_sales` GROUP BY `Date` ORDER BY `Date` DESC LIMIT 0,1) AS `sales`
;
'

echo $sql | docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --vertical | grep -v '^\*\*\*\*' | docker exec -i ${TAG_NAME:0:1}_telegram python /send_telegram.py

