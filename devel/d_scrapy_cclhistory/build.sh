#!/bin/bash

DIRNAME=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

docker build -t tknpoon/private:$TAG_NAME  $DIRNAME
