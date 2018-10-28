#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

#PORT25=`expr $PORTBASE + 25`

#
docker run \
 --name test_$TAG_NAME \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 --env-file $HOME/.self_env \
 -v $DIRNAME/testtest.py:/var/lib/scrapyd/testtest.py \
 -ti \
 --rm \
 vimagick/scrapyd  /usr/bin/python /var/lib/scrapyd/testtest.py

