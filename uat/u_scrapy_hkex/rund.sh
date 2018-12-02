#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

pattern=$(date +%y%m%d)
[ $# -gt 0 ] && pattern=$1

for hkexfile in `(cd $HOME/store/; find raw/hkex_gem -name e_G${pattern}\*htm\* ; find raw/hkex_quot -name d${pattern}\*.htm\* )`
do
 gzfile=`printf "/tmp/store/%s" $hkexfile`

 docker run \
 --name $TAG_NAME \
 --network ${TAG_NAME:0:1}_tptcn_overlay \
 --env-file $HOME/.self_env \
 -e URL_TO_SCRAP=file:///`basename $gzfile .gz` \
 -e STAGE=${TAG_NAME:0:1} \
 -e GZFILE=$gzfile \
 -v $CURDIR/entrypoint.py:/var/lib/scrapyd/entrypoint.py \
 -v $HOME/store:/tmp/store \
 -d --rm \
 tknpoon/private:${TAG_NAME} \
 /bin/bash -c 'gunzip -c $GZFILE > /`basename $GZFILE .gz`; scrapy runspider /var/lib/scrapyd/entrypoint.py'

 echo ====== Done working on $url `date`
done
