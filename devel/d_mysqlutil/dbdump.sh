#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

STAGE=${TAG_NAME:0:1}

CMD="mysqldump -u\$MYSQL_USER -p\"\$MYSQL_PASSWORD\" \$MYSQL_DATABASE $@"

docker exec -i \
  g_mysql \
  bash -c "exec $CMD" \
   | sed -e 's/),(/),\n(/g'

