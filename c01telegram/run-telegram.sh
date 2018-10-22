#!/bin/bash
#. $HOME/.self_env

CONTAINER_NAME=c01telegram

docker run \
 --name $CONTAINER_NAME \
 --env-file $HOME/.self_env \
 -p 11025:25 \
 -d \
 --restart=always \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py

# -e TOKEN=$TELEGRAM_TOKEN \
# -e CHAT_ID=$TELEGRAM_CHAT_ID \
