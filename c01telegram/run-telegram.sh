#!/bin/bash
CONTAINER_NAME=c01telegram

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker run \
 --name $CONTAINER_NAME \
 -e TOKEN='405736720:AAEvJ1Sza0_csF6CZ8uORLmeeguG7O1y0-8' \
 -e CHAT_ID='386573013' \
 -p 11025:1025 \
 -d \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py

