#!/bin/bash

apt-get remove docker docker-engine docker.io

apt-get update
apt-get install -y apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

apt-key fingerprint 0EBFCD88
add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

apt-get update
apt-get install -y docker-ce

usermod -aG docker ubuntu

echo 'Remember logout and login to enable docker. And then run "docker login"'
