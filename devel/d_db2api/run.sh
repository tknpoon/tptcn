#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT3000=`expr $PORTBASE + 3000`

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$TAG_NAME

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -e DB_HOST=${TAG_NAME:0:2}mysql \
 -e DB_DATABASE=${TAG_NAME:0:2}master \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 -d \
 -p ${PORT3000}:3000 \
reduardo7/db-to-api
