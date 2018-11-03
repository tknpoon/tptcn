#!/bin/bash
#. $HOME/.self_env

CURDIR=`cd $(dirname $0);pwd`
CONTAINER_NAME=$(basename `(cd $CURDIR; pwd)`)

VOLDIR=$HOME/vol/$CONTAINER_NAME
SCRIPTDIR=$CURDIR/scripts

[ ! -d $VOLDIR/vol-working ] && mkdir -p $VOLDIR/vol-working

docker run \
 -v $VOLDIR/vol-working:/working \
 -v $SCRIPTDIR:/scripts \
 --link g_mysql:db \
 --env-file $HOME/.self_env \
 --rm -i \
 tknpoon/private:$CONTAINER_NAME \
 bash -c 'mysql --host=db --database=$MYSQL_DATABASE --user=$MYSQL_USER --password=$MYSQL_PASSWORD < /scripts/replace_yahoo.sql'

