#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME


docker exec \
 $CONTAINER_NAME \
 bash -c 'exec mysqldump --no-data $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"' \
  > $CURDIR/vol-initdb/secmaster-01-structure.sql
# -e MYSQL_DATABASE=secmaster \
# -e MYSQL_USER=$MYSQL_USER -e MYSQL_PASSWORD=$MYSQL_PASSWORD \

