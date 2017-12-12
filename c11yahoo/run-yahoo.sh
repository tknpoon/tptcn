#!/bin/bash
. $HOME/.self_env

CURDIR=`cd $(dirname $0);pwd`
CONTAINER_NAME=$(basename `(cd $CURDIR; pwd)`)

VOLDIR=$HOME/vol/$CONTAINER_NAME
SCRIPTDIR=$CURDIR/scripts

[ ! -d $VOLDIR/vol-working ] && mkdir -p $VOLDIR/vol-working

docker run \
 -v $VOLDIR/vol-working:/working \
 -v $SCRIPTDIR:/scripts \
 --name $CONTAINER_NAME \
 --rm -ti \
 tknpoon/private:$CONTAINER_NAME \
 python /scripts/yahoo.py
