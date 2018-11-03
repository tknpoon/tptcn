#!/bin/bash

CONTAINER_NAME=g_mysql

CURDIR=`cd $(dirname $0); pwd`

for s in $CURDIR/sql/*sql;do
  echo =============== working on $s `date`
  cat $s | \
    docker exec -i \
      $CONTAINER_NAME \
      bash -c 'mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
done

d=$(date +'%Y-%m-%d')
echo "call pHKEXquote('$d', '$d'); call pHKEXupdateOpen('$d', '$d');" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'

