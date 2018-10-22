#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

echo testertester | \
docker exec \
 -i $TAG_NAME \
 python /send_telegram.py

