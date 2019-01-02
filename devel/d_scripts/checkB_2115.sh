#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

sql='
USE `p_master`;
SELECT MAX(`Date`) AS `today` FROM `consolidated_daily` ;
SELECT `symbol`,`Close`,`VWAP` FROM `consolidated_daily` 
WHERE `symbol` IN (SELECT `symbol` FROM `diary` WHERE SUBSTRING(`radar`,-2,1)='1')
  AND `Date` >= (SELECT MAX(`Date`) FROM `consolidated_daily` )
ORDER BY `symbol`
;
'
echo $sql | docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --vertical | grep -v '^\*\*\*\*' | docker exec -i ${TAG_NAME:0:1}_telegram python /send_telegram.py
