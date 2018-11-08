#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

docker build -t tknpoon/private:$TAG_NAME $DIRNAME
