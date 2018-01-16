#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $CURDIR/vol-lib_scrapyd

docker run \
 -v $CURDIR/vol-lib_scrapyd:/var/lib/scrapyd \
 --link c04nginx:web \
 --link c02mysql:db \
 -e MYSQL_USER=$MYSQL_USER \
 -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
 -e MYSQL_DB=$MYSQL_DB \
 -e PYTHONDONTWRITEBYTECODE=true \
 --rm \
 -ti \
 tknpoon/private:c05scrapyd \
 scrapy runspider /var/lib/scrapyd/work_today.py
