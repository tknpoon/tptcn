#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT3000=`expr $PORTBASE + 3000 `

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$TAG_NAME

THE_DB=${TAG_NAME:0:1}_master

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -e DB_HOST=g_mysql \
 -e DB_DATABASE=$THE_DB \
 --network ${TAG_NAME:0:1}_tptcn_overlay \
 -d --rm \
 -p $(ifconfig -a | grep inet|grep 192.168.8.|cut -d: -f2|cut -d' ' -f1):${PORT3000}:3000 \
reduardo7/db-to-api

