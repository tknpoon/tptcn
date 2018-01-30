#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`

for s in $CURDIR/sql/*sql;do
  echo =============== working on $s `date`
  cat $s | \
    docker exec -i \
      $CONTAINER_NAME \
      bash -c 'mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
done
