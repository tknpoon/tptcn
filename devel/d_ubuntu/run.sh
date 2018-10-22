#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -d --rm \
 --network d_tptcn_overlay \
 tknpoon/private:$TAG_NAME \
 sleep infinity