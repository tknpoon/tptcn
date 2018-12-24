#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

cat $DIRNAME/`basename $0 .sh`.py \
| docker exec -ti $TAG_NAME \
 /bin/bash -c 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib ; python -'
