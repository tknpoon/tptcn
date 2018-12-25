#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

PORT=`expr $PORTBASE + 8888`

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -p ${PORT}:8888 \
 -d --rm \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 -v $(cd $DIRNAME/..;pwd)/${TAG_NAME:0:1}_notebooks:/home/ubuntu/notebooks \
 tknpoon/private:$TAG_NAME \
 /bin/bash -c 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib ; jupyter notebook --allow-root --notebook-dir=/home/ubuntu/notebooks --ip=0.0.0.0 --port=8888 --no-browser'
