#!/bin/bash


DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)
#TAG_NAME=d_telegram

docker exec \
 $TAG_NAME \
 sendemail -f frommail@tknpoon -t someone@somewhere.com -s $TAG_NAME -m "test test"


