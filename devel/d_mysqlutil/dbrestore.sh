#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

STAGE=${TAG_NAME:0:1}

THE_DB=${STAGE}_master
CMD="mysql -uroot -p\$MYSQL_ROOT_PASSWORD $THE_DB $@"

docker exec -i \
  g_mysql \
  bash -c "exec $CMD" \

