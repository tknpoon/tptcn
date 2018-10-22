#!/bin/bash
dd if=/dev/zero of=/swapfile bs=1024k count=1024
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
