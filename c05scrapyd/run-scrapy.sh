#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $VOLDIR/vol-lib_scrapyd

docker run \
 --env-file $HOME/.self_env \
 -v $VOLDIR/vol-lib_scrapyd:/var/lib/scrapyd \
 --link c04nginx:web \
 --link c02mysql:db \
 --rm \
 -ti \
 vimagick/scrapyd \
 scrapy runspider /var/lib/scrapyd/d180105e.py
