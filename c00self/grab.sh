#!/bin/bash
set -a 
. $HOME/.self_env
####
function dl {
    url=$1
    dest=$2
    echo $url
    echo $dest
    code=`curl -A "Mozilla/5.0" -o $dest --silent --write-out '%{http_code}\n' $url`
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

#hkma
url=`date -d $dstr +https://www.hkma.gov.hk/eng/market-data-and-statistics/monetary-statistics/monetary-base/%Y/%Y%m%d-2.shtml`
[ ! -d ~/store/raw/hkma/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkma/$(date -d $dstr +%Y)
dlzip $url ~/store/raw/hkma/$(date -d $dstr +%Y)/moneybase$(basename $url .shtml).html

#hkex_quot
url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/smstat/dayquot/d%y%m%de.htm`
[ ! -d ~/store/raw/hkex_quot/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkex_quot/$(date -d $dstr +%Y)
dlzip $url ~/store/raw/hkex_quot/$(date -d $dstr +%Y)/$(basename $url)

#hkex_gem
url=`date -d $dstr +http://www.hkgem.com/statistics/daily/e_G%y%m%d.htm`
[ ! -d ~/store/raw/hkex_gem/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkex_gem/$(date -d $dstr +%Y)
dlzip $url ~/store/raw/hkex_gem/$(date -d $dstr +%Y)/$(basename $url)

#hhio
url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhio%y%m%d.zip`
[ ! -d ~/store/raw/hkex_hhio/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkex_hhio/$(date -d $dstr +%Y)
dl $url ~/store/raw/hkex_hhio/$(date -d $dstr +%Y)/$(basename $url)

#hhio
url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsio%y%m%d.zip`
[ ! -d ~/store/raw/hkex_hsio/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkex_hsio/$(date -d $dstr +%Y)
dl $url ~/store/raw/hkex_hsio/$(date -d $dstr +%Y)/$(basename $url)

#dqe
url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/dqe%y%m%d.zip`
[ ! -d ~/store/raw/hkex_stko/$(date -d $dstr +%Y) ] && mkdir -p ~/store/raw/hkex_stko/$(date -d $dstr +%Y)
dl $url ~/store/raw/hkex_stko/$(date -d $dstr +%Y)/$(basename $url)


