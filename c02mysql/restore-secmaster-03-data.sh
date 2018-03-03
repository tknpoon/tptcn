#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME


gunzip -c ~/data/secmaster-03-data.sql.gz \
| docker exec -i \
 $CONTAINER_NAME \
 bash -c 'exec mysql -u$MYSQL_USER -p"$MYSQL_PASSWORD" $MYSQL_DATABASE ' 

