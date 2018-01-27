#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec \
 $CONTAINER_NAME \
 bash -c 'mysqldump --no-data $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"; \
   mysqldump --routines --no-data $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD";' \
  > $CURDIR/vol-initdb/secmaster-01-structure.sql
