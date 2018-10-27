#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

[ "${TAG_NAME:0:2}" == "d_" ] && PORTBASE=20000
[ "${TAG_NAME:0:2}" == "u_" ] && PORTBASE=30000
[ "${TAG_NAME:0:2}" == "p_" ] && PORTBASE=40000
[ "${TAG_NAME:0:2}" == "g_" ] && PORTBASE=50000

#PORT25=`expr $PORTBASE + 25`

#
url=http://202.72.14.52/p2/cci/SearchHistory.aspx

docker run \
 --name $TAG_NAME \
 --network ${TAG_NAME:0:2}tptcn_overlay \
 --env-file $HOME/.self_env \
 -e URL_TO_SCRAP=$url \
 -v $DIRNAME/cclhistory.py:/var/lib/scrapyd/cclhistory.py \
 -ti \
 --rm \
 vimagick/scrapyd \
 /bin/bash -c 'scrapy runspider /var/lib/scrapyd/cclhistory.py '
