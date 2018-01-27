#!/bin/bash

docker run \
 --name c02myadmin \
 --link c02mysql:db \
 --env-file $HOME/.self_env \
 -d \
 -p 12080:80 \
phpmyadmin/phpmyadmin

