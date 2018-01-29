#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`

for s in $CURDIR/sql/*sql;do
  echo =============== working on $s
  cat $s | \
    docker exec \
      $CONTAINER_NAME \
      bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
done
