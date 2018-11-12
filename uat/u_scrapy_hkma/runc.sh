#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000


today=base$(date +%Y%m%d)
#today=base20181107
for hkmafile in `(cd $HOME/store/; find raw/hkma -name \*${today}\*html\*)`
do
 #url=`printf "http://${TAG_NAME:0:1}_nginx/%s" $hkmafile | sed -e 's/.gz$//'`
 #url=`printf "file:///127.0.0.1/tmp/store/%s" $hkmafile | sed -e 's/.gz$//'`
 gzfile=`printf "/tmp/store/%s" $hkmafile`

 docker run \
 --name $TAG_NAME \
 --network ${TAG_NAME:0:1}_tptcn_overlay \
 --env-file $HOME/.self_env \
 -e URL_TO_SCRAP=file:///`basename $gzfile .gz` \
 -e STAGE=${TAG_NAME:0:1} \
 -e GZFILE_TO_SCRAP=$gzfile \
 -v $CURDIR/entrypoint.py:/var/lib/scrapyd/entrypoint.py \
 -v $HOME/store:/tmp/store \
 --rm \
 tknpoon/private:$TAG_NAME \
 /bin/bash -c 'cp $GZFILE_TO_SCRAP / ; cd /;gunzip `basename $GZFILE_TO_SCRAP`; scrapy runspider /var/lib/scrapyd/entrypoint.py'
done
