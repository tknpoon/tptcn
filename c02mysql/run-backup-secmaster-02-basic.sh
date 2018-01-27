#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME


docker exec \
 $CONTAINER_NAME \
 bash -c 'exec mysqldump --no-create-info $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD" tSymbol tVendor' \
  > $CURDIR/vol-initdb/secmaster-02-basic.sql

