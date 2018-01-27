#!/bin/bash
set -a
. $HOME/.self_env

CONTAINER_NAME=g00temp

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 -v $VOLDIR/vol-datadir:/scrapyproj \
 --link c02mysql:db \
 --env-file $HOME/.self_env \
 --name $CONTAINER_NAME \
 --rm -ti \
 tknpoon/private:$CONTAINER_NAME \
 python /testmy.py

