#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`

echo "SELECT * FROM tDailyPrice; " | \
  docker exec -i  $CONTAINER_NAME \
    bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD" | sed "s/\t/\,/g" ' \
| gzip -c > $HOME/store/result/tDailyPrice.csv.gz

