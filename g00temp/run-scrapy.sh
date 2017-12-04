#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=g00temp

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 -v $VOLDIR/vol-datadir:/scrapyproj \
 --name $CONTAINER_NAME \
 -d \
 tknpoon/private:$CONTAINER_NAME \
 bash -c 'while [ 1 ]; do sleep 5; done'

