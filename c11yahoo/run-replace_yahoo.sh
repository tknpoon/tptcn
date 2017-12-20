#!/bin/bash
. $HOME/.self_env

CURDIR=`cd $(dirname $0);pwd`
CONTAINER_NAME=$(basename `(cd $CURDIR; pwd)`)

VOLDIR=$HOME/vol/$CONTAINER_NAME
SCRIPTDIR=$CURDIR/scripts

[ ! -d $VOLDIR/vol-working ] && mkdir -p $VOLDIR/vol-working

docker run \
 -v $VOLDIR/vol-working:/working \
 -v $SCRIPTDIR:/scripts \
 --link c02mysql:db \
 -e MYSQL_USER=$MYSQL_USER \
 -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
 -e MYSQL_DB=$MYSQL_DB \
 --rm -i \
 tknpoon/private:$CONTAINER_NAME \
 bash -c "mysql --host=db --database=$MYSQL_DB --user=$MYSQL_USER --password=$MYSQL_PASSWORD < /scripts/replace_yahoo.sql"
