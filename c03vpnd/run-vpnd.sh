#!/bin/bash
. $HOME/.self_env

sudo modprobe af_key

CONTAINER_NAME=c03vpnd

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME
CHAPSECRET=${VOLDIR}/vol-datadir/chap-secret

docker run \
 --name c03vpnd \
 --env-file $HOME/.self_env \
 --restart=always \
 -p 500:500/udp \
 -p 4500:4500/udp \
 -v /lib/modules:/lib/modules:ro \
 -d --privileged \
 hwdsl2/ipsec-vpn-server
