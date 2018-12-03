#!/bin/bash
DIRNAME=`cd $(dirname $0); pwd`
#CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

#VOLDIR=$HOME/vol/$TAG_NAME
#CHAPSECRET=${VOLDIR}/vol-datadir/chap-secret

sudo modprobe af_key

docker run \
 --name $TAG_NAME \
 --env-file $HOME/.self_env \
 --restart=always \
 -p 500:500/udp \
 -p 4500:4500/udp \
 -v /lib/modules:/lib/modules:ro \
 -d --privileged \
 hwdsl2/ipsec-vpn-server
