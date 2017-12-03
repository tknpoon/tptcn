#!/bin/bash
<<<<<<< HEAD

. $HOME/.self_env

=======
. $HOME/.self_env

>>>>>>> 97409e308f01459a0608131cb91a06a784b75ba2
CONTAINER_NAME=c01telegram

docker run \
 --name $CONTAINER_NAME \
 -e TOKEN=$TELEGRAM_TOKEN \
 -e CHAT_ID=$TELEGRAM_CHAT_ID \
 -p 11025:25 \
 -d \
 tknpoon/private:$CONTAINER_NAME \
 python /telegram.py
