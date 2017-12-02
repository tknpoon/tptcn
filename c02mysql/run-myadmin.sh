#!/bin/bash


docker run \
 --name c02myadmin \
 --link c02mysql:db \
 -d \
 -p 12080:80 \
phpmyadmin/phpmyadmin

