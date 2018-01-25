#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

stmt="ALTER TABLE tHKEX_Quotation DROP Open "

stmt="
ALTER TABLE tHKEX_Quotation 
 CHANGE Name Name VARCHAR(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
 CHANGE PrevClose PrevClose DECIMAL(10,3) NULL DEFAULT NULL,
 CHANGE High High DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Low Low DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Close Close DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Bid Bid DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Ask Ask DECIMAL(10,3) NULL DEFAULT NULL;
"

stmt="ALTER TABLE tHKEX_Sales 
 CHANGE Serial Serial VARCHAR(7) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL, 
 CHANGE Price Price DECIMAL(10,3) NULL DEFAULT NULL;
"

echo "$stmt" | \
docker exec -i \
  $CONTAINER_NAME \
  bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'