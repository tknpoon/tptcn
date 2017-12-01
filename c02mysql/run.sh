#!/bin/bash

docker run --name c02mysql \
  -e MYSQL_ROOT_PASSWORD=useItOnce \
  -e MYSQL_ONETIME_PASSWORD=1 \
  -d mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci
