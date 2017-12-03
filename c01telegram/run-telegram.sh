#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c01telegram

docker run \
 --name $CONTAINER_NAME \
 -e TOKEN=$TELEGRAM_TOKEN \
 -e CHAT_ID=$TELEGRAM_CHAT_ID \
 -p 11025:25 \
 -d \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py
