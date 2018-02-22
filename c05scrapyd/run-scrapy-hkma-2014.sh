#!/bin/bash

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $CURDIR/vol-lib_scrapyd

today=base2014

for u in `(cd $HOME/store/; find raw/hkma -name \*${today}\*html\*)`
do
  url=`printf "http://web/%s" $u | sed -e 's/.gz$//'`
  echo $url

  docker run \
   -v $CURDIR/vol-lib_scrapyd:/var/lib/scrapyd \
   --link c04nginx:web \
   --link c02mysql:db \
   --env-file $HOME/.self_env \
   -e URL_TO_SCRAP=$url \
   --rm \
   tknpoon/private:c05scrapyd \
   scrapy runspider /var/lib/scrapyd/hkma.py

  echo ====== Done working on $url `date`
done
