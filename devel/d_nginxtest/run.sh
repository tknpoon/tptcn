#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT80=`expr $PORTBASE + 80`

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -d --rm \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 -p ${PORT80}:80 \
 nginx:alpine
