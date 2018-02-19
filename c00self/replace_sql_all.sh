#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`

echo "truncate tDailyPrice;" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'

for s in $CURDIR/sql/*sql;do
  echo =============== working on $s `date`
  cat $s | \
    docker exec -i \
      $CONTAINER_NAME \
      bash -c 'mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
done

fd=1990-01-01
td=$(date +'%Y-%m-%d')
echo "call pHKEXquote('$fd', '$td'); call pHKEXupdateOpen('$fd', '$td');" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'

