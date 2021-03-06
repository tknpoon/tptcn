#!/bin/bash

DIRNAME=`dirname $0`
CURDIR=$(cd $DIRNAME ; pwd)
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

docker run \
 --env-file $HOME/.self_env \
 -e TAG_NAME=${TAG_NAME} \
 -e STAGE=${TAG_NAME:0:1} \
 -ti --rm \
 -v ${CURDIR}/test.py:/test.py \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 tknpoon/private:$TAG_NAME \
 python /test.py
