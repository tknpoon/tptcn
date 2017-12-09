#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-lib_scrapyd ] && mkdir -p $VOLDIR/vol-lib_scrapyd

docker run \
 -v $CURDIR/scrapyd.conf:/etc/scrapyd/scrapyd.conf \
 -v $VOLDIR/vol-lib_scrapyd:/var/lib/scrapyd \
 --link c04nginx:web \
 --link c02mysql:db \
 --name $CONTAINER_NAME \
 -p 15680:6800 \
 -d \
 tknpoon/private:c05scrapyd
