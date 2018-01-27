#!/bin/bash

CONTAINER_NAME=c04nginx

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 -v $HOME/store:/usr/share/nginx/html:ro \
 -v $CURDIR/nginx-default.conf:/etc/nginx/conf.d/default.conf:ro \
 --name c04nginx \
 --env-file $HOME/.self_env \
 -d \
 --restart=always \
 -p 14080:80 \
 nginx
