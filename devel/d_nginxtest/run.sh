#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 -d --rm \
 --network my-attachable-overlay \
 -p 20080:80 \
 nginx:alpine

