#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

theurl='https://www.reuters.com/finance/commodity'

today=$(date +%y%m%d)

docker run \
--name $TAG_NAME \
--network ${TAG_NAME:0:1}_tptcn_overlay \
--env-file $HOME/.self_env \
-e URL_TO_SCRAP=$theurl \
-e STAGE=${TAG_NAME:0:1} \
-v $CURDIR/entrypoint.py:/var/lib/scrapyd/entrypoint.py \
-v $HOME/store:/tmp/store \
--rm \
tknpoon/private:${TAG_NAME} \
scrapy runspider /var/lib/scrapyd/entrypoint.py

echo ====== Done working on $theurl `date`
