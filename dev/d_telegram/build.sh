#!/bin/bash

DIRNAME=`dirname $0`
CON_NAME=$(cd $DIRNAME ; basename `pwd`)

docker build -t tknpoon/private:$CON_NAME $DIRNAME
