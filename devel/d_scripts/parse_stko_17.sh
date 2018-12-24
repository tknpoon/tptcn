#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)
BNAME=parse_stko

yy=17

for i in $HOME/store/raw/hkex_stko/20${yy}/dqe${yy}*.zip
do
  if [ -f $i ]; then
    echo $i
    docker run \
    --env-file $HOME/.self_env \
    -e STAGE=${TAG_NAME:0:1} \
    -i --rm \
    --network ${TAG_NAME:0:2}tptcn_overlay \
    -v $(cd $DIRNAME/;pwd)/${BNAME}.py:/tmp/entrypoint.py \
    -v $i:/tmp/entrypoint.zip \
    tknpoon/private:${TAG_NAME:0:1}_anaconda \
    /bin/bash -c 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib;python /tmp/entrypoint.py'
  fi
done

