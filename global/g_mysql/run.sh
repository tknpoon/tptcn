#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT3306=`expr $PORTBASE + 3306`

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$TAG_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

vv=""
#[ ! -d $CURDIR/vol-initdb ]  && mkdir -p $CURDIR/vol-initdb
#for i in `find $CURDIR/vol-initdb/ -name \*.sql\*`  ; do
# vv="$vv -v $i:/docker-entrypoint-initdb.d/`basename $i`"
#done

docker run \
 -v $VOLDIR/vol-datadir:/var/lib/mysql \
 $vv \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -e MYSQL_DATABASE=${TAG_NAME:0:1}_master \
 -d \
 --network ${TAG_NAME:0:1}_tptcn_overlay \
 -p $PORT3306:3306 \
 --restart=always \
 mysql:5.7 \
 --character-set-server=utf8mb4 \
 --collation-server=utf8mb4_unicode_ci

sleep 10
docker network connect d_tptcn_overlay $TAG_NAME
docker network connect u_tptcn_overlay $TAG_NAME
docker network connect p_tptcn_overlay $TAG_NAME
#Usage:  docker network connect [OPTIONS] NETWORK CONTAINER

