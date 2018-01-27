#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir
[ ! -d $CURDIR/vol-initdb ]  && mkdir -p $CURDIR/vol-initdb

docker run \
 -v $VOLDIR/vol-datadir:/var/lib/mysql \
 -v $CURDIR/vol-initdb:/docker-entrypoint-initdb.d \
 --name $CONTAINER_NAME \
 --env-file $HOME/.self_env \
 -p 12336:3306 \
 -d \
 --restart=always \
 mysql:5.7 \
 --character-set-server=utf8mb4 \
 --collation-server=utf8mb4_unicode_ci

