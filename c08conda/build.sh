#!/bin/bash

CURDIR=`cd $(dirname $0);pwd`
CONTAINER_NAME=$(basename `(cd $CURDIR; pwd)`)

docker build -t tknpoon/private:${CONTAINER_NAME} `dirname $0`
