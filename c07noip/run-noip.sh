#!/bin/bash

docker run \
 --name c07noip \
 --env-file $HOME/.self_env \
 -d --rm \
 -v /etc/localtime:/etc/localtime \
 -v $HOME/vol/c07noip:/config \
 coppit/no-ip



