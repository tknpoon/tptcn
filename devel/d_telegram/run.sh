#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -p 10025:25 \
 -d \
 --restart=always \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py
