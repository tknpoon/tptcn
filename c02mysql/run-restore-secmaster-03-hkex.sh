#!/bin/bash
. $HOME/.self_env

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME


gunzip -c ~/data/secmaster-03-hkex.sql.gz \
| docker exec \
 $CONTAINER_NAME \
 bash -c 'exec mysql -u$MYSQL_USER -p"$MYSQL_PASSWORD" ' 

