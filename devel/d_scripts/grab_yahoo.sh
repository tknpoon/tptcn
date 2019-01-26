#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)
BNAME=$(basename $0 .sh)

docker run \
--env-file $HOME/.self_env \
-e STAGE=${TAG_NAME:0:1} \
--rm \
--network ${TAG_NAME:0:2}tptcn_overlay \
-v $(cd $DIRNAME/;pwd)/${BNAME}.py:/tmp/entrypoint.py \
tknpoon/private:${TAG_NAME:0:1}_anaconda \
/bin/bash -c 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib;python /tmp/entrypoint.py $*'

