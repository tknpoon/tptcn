#!/bin/bash
#. $HOME/.self_env

DIRNAME=`dirname $0`
CON_NAME=$(cd $DIRNAME ; basename `pwd`)

docker run \
 --name $CON_NAME \
 --env-file $HOME/.self_env \
 -p 10025:25 \
 -d \
 --restart=always \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py
