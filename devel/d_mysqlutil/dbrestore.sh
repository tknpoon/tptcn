#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

STAGE=${TAG_NAME:0:1}

THE_DB=${STAGE}_master
<<<<<<< HEAD
CMD="mysql -uroot -p\"\$MYSQL_ROOT_PASSWORD\" $THE_DB $@"
=======
CMD="mysql -uroot -p\$MYSQL_ROOT_PASSWORD $THE_DB $@"
>>>>>>> 540a1aef18164eedf033e15ce9b6916666b4f488

docker exec -i \
  g_mysql \
  bash -c "exec $CMD" \

