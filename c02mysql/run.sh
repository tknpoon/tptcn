#!/bin/bash

docker run --name c02mysql \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  -d mysql:5.7 \  -d mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci

$ docker run --name some-mysql -v /my/custom:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

