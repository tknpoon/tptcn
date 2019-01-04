#!/bin/bash
set -a 
. $HOME/.self_env
####
function dl {
    url=$1
    dest=$2
    echo "$url"
    echo "$dest"
    code=`curl -L -A "Mozilla/5.0" -o $dest --silent --write-out '%{http_code}\n' "$url"`
    [ $code -eq 404 ] && [ -f $dest ] && rm -f $dest
    echo $code
}

####
function dlzip {
    url="$1"
    dest="$2"
    dl "$url" "$dest"
    [ -f "$dest" ] &&  gzip --force "$dest"
}

#### main
if [ $# -gt 0 ]; then
  dstr=$1
else
  dstr=`date +%Y%m%d`
fi

#hkab
url=`date -d $dstr +http://www.hkab.org.hk/hibor/listRates.do\?lang=en\&Submit=Search\&year=%Y\&month=%m\&day=%d`
[ ! -d ~/store/raw/hkab/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkab/$(date -d $dstr +%Y)
dlzip "$url" ~/store/raw/hkab/$(date -d $dstr +%Y)/$(date -d $dstr +hkab%Y%m%d.htm)

