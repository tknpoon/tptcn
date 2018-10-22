#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT3306=`expr $PORTBASE + 3306`

####################################
vv=""
for i in `ls $DIRNAME/vol-initdb/ | grep \.sql`; do
 vv="$vv -v $CURDIR/vol-initdb/`basename $i`:/docker-entrypoint-initdb.d/`basename $i`"
done
#for i in `ls $HOME/data/ | grep \.sql` ; do
# vv="$vv -v $HOME/data/`basename $i`:/docker-entrypoint-initdb.d/`basename $i`"
#done

####################################
docker run \
 -v $VOLDIR/vol-datadir:/var/lib/mysql \
 $vv \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -p ${PORT3306}:3306 \
 -d \
 --restart=always \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 mysql:5.7 \
 --character-set-server=utf8mb4 \
 --collation-server=utf8mb4_unicode_ci
