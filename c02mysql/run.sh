#!/bin/bash
CURDIR=$(dirname $0)
docker run \
  -v $CURDIR/vol-datadir:/var/lib/mysql \
  -v $CURDIR/vol-initdb:/docker-entrypoint-initdb.d \
  --name c02mysql \
  -e MYSQL_ROOT_PASSWORD=useItOnce \
  -e MYSQL_ONETIME_PASSWORD=1 \
  -e MYSQL_DATABASE=secmaster \
  -d \
  mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci
