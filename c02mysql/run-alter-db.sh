#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

docker exec -t \
  $CONTAINER_NAME \
  bash -c '\
    echo "
USE secmaster;
ALTER TABLE tHKEX_Sales 
 CHANGE Flag Flag VARCHAR(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
 CHANGE Price Price DECIMAL(10,3) NULL DEFAULT NULL;
" | exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD" \
'

