#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec \
 $CONTAINER_NAME \
 bash -c 'echo USE secmaster\; ; echo; exec mysqldump \
 -u$MYSQL_USER -p"$MYSQL_PASSWORD" \
 --add-drop-table \
 --databases $MYSQL_DATABASE \
 --tables \
  tTR_Daily \
  tYAHOO_Daily \
  tHKEX_Quotation \
  tHKEX_Sales \
' | gzip > ~/data/secmaster-03-hkex.sql.gz

