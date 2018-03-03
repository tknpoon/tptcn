#!/bin/bash

docker run \
 -ti --name c06onedrive \
 --restart on-failure \
 -v $HOME/vol/c06onedrive/onedrive:/onedrive \
 -v $HOME/vol/c06onedrive/sync_list:/root/.config/onedrive/sync_list \
 kukki/docker-onedrive

