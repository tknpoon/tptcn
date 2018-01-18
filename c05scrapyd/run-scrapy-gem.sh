#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c05scrapyd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $CURDIR/vol-lib_scrapyd ] && mkdir -p $CURDIR/vol-lib_scrapyd

#today=180117
today=1

#for u in `(cd $HOME/store/; find raw/hkex_gem -name \*${today}\*htm\*; find raw/hkex_quot -name \*${today}\*htm\*)`
for u in `(cd $HOME/store/; find raw/hkex_gem -name \*${today}\*htm\*)`
do
  url=`printf "http://web/%s" $u | sed -e 's/.gz$//'`

  docker run \
   -v $CURDIR/vol-lib_scrapyd:/var/lib/scrapyd \
   --link c04nginx:web \
   --link c02mysql:db \
   -e MYSQL_USER=$MYSQL_USER \
   -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
   -e MYSQL_DB=$MYSQL_DB \
   -e URL_TO_SCRAP=$url \
   -e PYTHONDONTWRITEBYTECODE=true \
   --rm \
   -t \
   tknpoon/private:c05scrapyd \
   scrapy runspider /var/lib/scrapyd/work1.py

  echo ====== Done working on $url
done
