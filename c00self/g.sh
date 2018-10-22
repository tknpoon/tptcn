#!/bin/bash
set -a 
. $HOME/.self_env
####
function dl {
    url=$1
    dest=$2
    echo $url
    echo $dest
    code=`curl -L -A "Mozilla/5.0" -o $dest --silent --write-out '%{http_code}\n' $url`
    [ $code -eq 404 ] && [ -f $dest ] && rm -f $dest
    echo $code
}

####
function dlzip {
    url=$1
    dest=$2
    dl $url $dest
    [ -f $dest ] &&  gzip --force $dest
}

#### main
if [ $# -gt 0 ]; then
  dstr=$1
else
  dstr=`date +%Y%m%d`
fi

##hsi con
url=`date -d $dstr +https://www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/report/hsi/con_%-d%b%y.csv`
[ ! -d ~/store/raw/hsi ] && mkdir -p ~/store/raw/hsi
dlzip $url ~/store/raw/hsi/$(basename $url)

##hsi idx perf
url=`date -d $dstr +https://www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/Index_Performance_Summary_%-d%b%y.xls`
[ ! -d ~/store/raw/hsi ] && mkdir -p ~/store/raw/hsi
dlzip $url ~/store/raw/hsi/$(basename $url)

