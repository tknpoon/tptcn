#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $CURDIR/vol-lib_scrapyd

for u in `(cd $HOME/store/; find raw/hkex_quot/2018 -name d\*htm\*)`
do
  url=`printf "http://web/%s" $u | sed -e 's/.gz$//'`

  docker run \
   -v $CURDIR/vol-lib_scrapyd:/var/lib/scrapyd \
   --link c04nginx:web \
   --link c02mysql:db \
   -e MYSQL_USER=$MYSQL_USER \
   -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
   -e MYSQL_DB=$MYSQL_DB \
   -e PYTHONDONTWRITEBYTECODE=true \
   -e URL_TO_SCRAP=$url \
   --rm \
   -ti \
   tknpoon/private:c05scrapyd \
   scrapy runspider /var/lib/scrapyd/work.py
done
