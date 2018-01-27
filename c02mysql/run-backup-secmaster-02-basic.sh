#!/bin/bash
set -a
. $HOME/.self_env

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME


echo USE $MYSQL_DB \; > $CURDIR/vol-initdb/secmaster-02-basic.sql

docker exec \
 $CONTAINER_NAME \
 bash -c 'exec mysqldump --no-create-info -u$MYSQL_USER -p"$MYSQL_PASSWORD" \
  --databases $MYSQL_DB --tables \
   tSymbol \
   tSymbolMeta \
   tVendor \
' >> $CURDIR/vol-initdb/secmaster-02-basic.sql

