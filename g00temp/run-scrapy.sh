#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=g00temp

docker run \
 --name $CONTAINER_NAME \
 -ti \
 tknpoon/private:$CONTAINER_NAME \
 bash
