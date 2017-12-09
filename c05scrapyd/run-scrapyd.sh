#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-etc_scrapyd ] && mkdir -p $VOLDIR/vol-etc_scrapyd
[ ! -d $VOLDIR/vol-lib_scrapyd ] && mkdir -p $VOLDIR/vol-lib_scrapyd

docker run \
 -v $VOLDIR/vol-etc_scrapyd:/etc/scrapyd \
 -v $VOLDIR/vol-lib_scrapyd:/var/lib/scrapyd \
 --link c04nginx:web \
 --link c02mysql:db \
 --name $CONTAINER_NAME \
 -p 13680:6800 \
 -d \
 vimagick/scrapyd
