#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec \
 $CONTAINER_NAME \
 bash -c 'mysqldump --routines --no-data -u$MYSQL_USER -p"$MYSQL_PASSWORD" --databases $MYSQL_DATABASE ;' \
  > $CURDIR/vol-initdb/secmaster-01-structure.sql
