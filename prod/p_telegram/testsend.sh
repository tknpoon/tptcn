#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)
#TAG_NAME=d_telegram

docker exec \
 $TAG_NAME \


