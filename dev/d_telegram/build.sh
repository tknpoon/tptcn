#!/bin/bash

DIRNAME=`dirname $0`
CON_NAME=`basename $DNAME`

echo  docker build -t tknpoon/private:$CON_NAME $DIRNAME
