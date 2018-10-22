#!/bin/bash

CONTAINER_NAME=c08conda

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

[ ! -d $VOLDIR/vol-datadir ] && mkdir -p $VOLDIR/vol-datadir

docker run \
 --name $CONTAINER_NAME \
 --env-file $HOME/.self_env \
 -d \
 --restart=always \
 -p 18080:8888 \
 tknpoon/private:c08conda \
 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"
 
