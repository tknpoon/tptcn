#!/bin/bash

CONTAINER_NAME=g_mysql

CURDIR=`cd $(dirname $0); pwd`

echo "truncate tDailyPrice;" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql secmaster -u$MYSQL_USER -p"$MYSQL_PASSWORD"'

for s in $CURDIR/sql/*sql;do
  echo =============== working on $s `date`
  cat $s | \
    docker exec -i \
      $CONTAINER_NAME \
      bash -c 'mysql secmaster -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
done


fd=1990-01-01
td=$(date +'%Y-%m-%d')

echo =============== working on hkex quote on `date`
echo "call pHKEXquote('$fd', '$td');" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql secmaster -u$MYSQL_USER -p"$MYSQL_PASSWORD"'

echo =============== working on hkex open on `date`
echo "call pHKEXupdateOpen('$fd', '$td');" | \
  docker exec -i \
    $CONTAINER_NAME \
    bash -c 'exec mysql secmaster -u$MYSQL_USER -p"$MYSQL_PASSWORD"'


echo =============== working on export_data.sh `date`
/bin/bash /home/ubuntu/repo/tptcn/c00self/export_data.sh

echo 'done!!!'
