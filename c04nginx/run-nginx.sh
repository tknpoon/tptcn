#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c04nginx

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 -v $VOLDIR/vol-datadir:/usr/share/nginx/html:ro \
 -v $CURDIR/nginx-default.conf:/etc/nginx/conf.d/default.conf:ro \
 --name c04nginx \
 -d \
 --restart=always \
 -p 14080:80 \
 nginx
