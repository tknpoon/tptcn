#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c03scrapy

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-etc_scrapyd ] && mkdir -p $VOLDIR/vol-etc_scrapyd
[ ! -d $VOLDIR/vol-lib_scrapyd ] && mkdir -p $VOLDIR/vol-lib_scrapyd

docker run \
 -v $VOLDIR/vol-etc_scrapyd:/etc/scrapyd \ 
 -v $VOLDIR/vol-lib_scrapyd:/var/lib/scrapyd \
 --name $CONTAINER_NAME \
 -p 13680:6800 \
 -d \
 tknpoon/private:$CONTAINER_NAME

