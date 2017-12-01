#!/bin/bash

CURDIR=`cd $(dirname $0); pwd`

docker run \
  -v $CURDIR/vol-datadir:/var/lib/mysql \
  -v $CURDIR/vol-initdb:/docker-entrypoint-initdb.d \
  --name c02mysql \
  -e MYSQL_ROOT_PASSWORD=useItOnce \
  -e MYSQL_ONETIME_PASSWORD=1 \
  -e MYSQL_DATABASE=secmaster \
  -p 12336:3306 \
  -d \
  mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci
