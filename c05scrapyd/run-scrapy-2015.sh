#!/bin/bash

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $CURDIR/vol-lib_scrapyd
[ ! -d $VOLDIR/vol-lib_scrapyd ] && mkdir -p $VOLDIR/vol-lib_scrapyd

files=`(cd $HOME/store/; ls raw/hkex_quot/2015/*.gz)`
echo $files

for u in $files
do
  url=`printf "http://web/%s" $u | sed -e 's/.gz$//'`
  docker run \
   -v $CURDIR/vol-lib_scrapyd:/var/lib/scrapyd \
   -v $VOLDIR/vol-lib_scrapyd:/tmp/log \
   --link c04nginx:web \
   --link c02mysql:db \
   --env-file $HOME/.self_env \
   -e URL_TO_SCRAP=$url \
   --rm \
   tknpoon/private:c05scrapyd \
   /bin/bash -c 'scrapy runspider /var/lib/scrapyd/work1.py >/tmp/log/`basename $URL_TO_SCRAP`.log 2>&1 '

  echo ====== Done working on $url
done
