#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec \
 $CONTAINER_NAME \
 bash -c 'exec mysqldump --no-create-info -u$MYSQL_USER -p"$MYSQL_PASSWORD" --databases $MYSQL_DATABASE --tables \
 tDailyPrice \
 tTR_Daily \
 tYAHOO_Daily \
 tHKEX_Quotation \
 tHKEX_Sales \
' | gzip > ~/data/secmaster-03-hkex.sql.gz

