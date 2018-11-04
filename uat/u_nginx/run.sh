#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT80=`expr $PORTBASE + 80`

#
docker run \
 --name $TAG_NAME \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 --env-file $HOME/.self_env \
 -e STAGE=${TAG_NAME:0:1} \
 -v $HOME/store:/usr/share/nginx/html:ro \
 -v $CURDIR/nginx-default.conf:/etc/nginx/conf.d/default.conf:ro \
 -p ${PORT80}:80 \
 -d --restart=always \
 nginx
