#!/bin/bash
set -a
. $HOME/.self_env

CONTAINER_NAME=g01temp

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 -v $VOLDIR/vol-datadir:/scrapyproj \
 --name $CONTAINER_NAME \
 -p 12080:6800 \
 -d \
 vimagick/scrapyd
