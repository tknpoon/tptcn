#!/bin/bash

CURDIR=`cd $(dirname $0); pwd`

[ ! -d $CURDIR/vol-datadir ] && mkdir -p $CURDIR/vol-datadir
[ ! -d $CURDIR/vol-initdb ]  && mkdir -p $CURDIR/vol-initdb

docker run \
-v $CURDIR/vol-datadir:/var/lib/mysql \
-v $CURDIR/vol-initdb:/docker-entrypoint-initdb.d \
--name c02mysql \
-e MYSQL_DATABASE=secmaster \
-e MYSQL_ROOT_PASSWORD=useItOnce -e MYSQL_ONETIME_PASSWORD=yes \
-e MYSQL_USER=tptcn -e MYSQL_PASSWORD=tptcnpass \
-p 12336:3306 \
-d \
mysql:5.7 \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci

