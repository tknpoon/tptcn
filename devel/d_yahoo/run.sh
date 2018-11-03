#!/bin/bash

DIRNAME=`dirname $0`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

docker run \
 --name ${TAG_NAME}_`date +%s` \
 --env-file $HOME/.self_env \
 -e STAGE=${TAG_NAME:0:1} \
 -d --rm \
 -v ${CURDIR}/grab_yahoo.py:/grab_yahoo.py \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 tknpoon/private:$TAG_NAME \
 python /grab_yahoo.py 
