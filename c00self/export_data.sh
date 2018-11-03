#!/bin/bash

CONTAINER_NAME=g_mysql

CURDIR=`cd $(dirname $0); pwd`

echo "SELECT * FROM tDailyPrice; " | \
  docker exec -i  $CONTAINER_NAME \
    bash -c 'exec mysql secmaster -u$MYSQL_USER -p"$MYSQL_PASSWORD" | sed "s/\t/\,/g" ' \
| gzip -c > $HOME/store/result/tDailyPrice.csv.gz

