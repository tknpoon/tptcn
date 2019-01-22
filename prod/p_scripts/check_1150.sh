#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

sql='
USE `p_master`;
SELECT `Date`, `Overnight` AS `ON`, `1W`, `2W`, `1M`, `2M`, `3M`, `6M`, `12M` FROM `hkab` ORDER BY `Date` DESC LIMIT 0,2
;
'

echo $sql | docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --vertical | grep -v '^\*\*\*\*' | docker exec -i ${TAG_NAME:0:1}_telegram python /send_telegram.py

