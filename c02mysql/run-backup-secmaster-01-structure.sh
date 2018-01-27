#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec \
 $CONTAINER_NAME \
 bash -c 'mysqldump --databases --routines --no-data $MYSQL_DB -u$MYSQL_USER -p"$MYSQL_PASSWORD";' \
  > $CURDIR/vol-initdb/secmaster-01-structure.sql
