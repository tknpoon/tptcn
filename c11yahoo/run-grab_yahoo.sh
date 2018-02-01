#!/bin/bash
#. $HOME/.self_env

PARAM=$1

CURDIR=`cd $(dirname $0);pwd`
CONTAINER_NAME=$(basename `(cd $CURDIR; pwd)`)

VOLDIR=$HOME/vol/$CONTAINER_NAME
SCRIPTDIR=$CURDIR/scripts

[ ! -d $VOLDIR/vol-working ] && mkdir -p $VOLDIR/vol-working

docker run \
 -v $VOLDIR/vol-working:/working \
 -v $SCRIPTDIR:/scripts \
 --link c02mysql:db \
 --env-file $HOME/.self_env \
 --rm \
 tknpoon/private:$CONTAINER_NAME \
 python /scripts/grab_yahoo.py $PARAM
