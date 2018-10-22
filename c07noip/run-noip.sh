#!/bin/bash

THEVOL=c07noip
[ $(hostname) == tphome201 ] && THEVOL=c07noip-tphome201

docker run \
 --name c07noip \
 --env-file $HOME/.self_env \
 -d --rm \
 -v /etc/localtime:/etc/localtime \
 -v $HOME/vol/$THEVOL:/config \
 coppit/no-ip



