#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir
[ ! -d $CURDIR/vol-initdb ]  && mkdir -p $CURDIR/vol-initdb

vv=""
for i in $CURDIR/vol-initdb/*sql* $HOME/data/*sql*
do
 vv="$vv -v $CURDIR/vol-initdb/$i:/docker-entrypoint-initdb.d/$i"
done

docker run \
 -v $VOLDIR/vol-datadir:/var/lib/mysql \
 $vv \
 --name $CONTAINER_NAME \
 --env-file $HOME/.self_env \
 -p 12336:3306 \
 -d \
 --restart=always \
 mysql:5.7 \
 --character-set-server=utf8mb4 \
 --collation-server=utf8mb4_unicode_ci

