#!/bin/bash
set -a
. $HOME/.self_env

####
function check {
    url=$1
    dest=$2
    shortdest=`echo $dest | sed -e 's/\/home\/ubuntu\/store\/raw\///'`
    [ -f $dest ] && echo 1 $shortdest || echo 0 $shortdest
}

####
function checkzip {
    url=$1
    dest=$2
    check $url ${dest}.gz
}

####
function mainjob {
    dstr=$1
    ##hsi con
    url=`date -d $dstr +https://www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/report/hsi/con_%-d%b%y.csv`
    checkzip $url /home/ubuntu/store/raw/hsi/$(basename $url)

    ##hsi idx perf
    url=`date -d $dstr +https://www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/Index_Performance_Summary_%-d%b%y.xls`
    checkzip $url /home/ubuntu/store/raw/hsi/$(basename $url)

    #hkma
    url=`date -d $dstr +http://www.hkma.gov.hk/eng/market-data-and-statistics/monetary-statistics/monetary-base/%Y/%Y%m%d-2.shtml`
    checkzip $url /home/ubuntu/store/raw/hkma/$(date -d $dstr +%Y)/moneybase$(basename $url .shtml).html

    #hkex_quot
    url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/smstat/dayquot/d%y%m%de.htm`
    checkzip $url /home/ubuntu/store/raw/hkex_quot/$(date -d $dstr +%Y)/$(basename $url)

    #hkex_gem
    url=`date -d $dstr +http://www.hkgem.com/statistics/daily/e_G%y%m%d.htm`
    checkzip $url /home/ubuntu/store/raw/hkex_gem/$(date -d $dstr +%Y)/$(basename $url)

    #hhio
    url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhio%y%m%d.zip`
    check $url /home/ubuntu/store/raw/hkex_hhio/$(date -d $dstr +%Y)/$(basename $url)

    #hhio
    url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsio%y%m%d.zip`
    check $url /home/ubuntu/store/raw/hkex_hsio/$(date -d $dstr +%Y)/$(basename $url)

    #dqe
    url=`date -d $dstr +http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/dqe%y%m%d.zip`
    check $url /home/ubuntu/store/raw/hkex_stko/$(date -d $dstr +%Y)/$(basename $url)
}
#### main
if [ $# -gt 0 ]; then
  dstr=$1
else
  dstr=`date +%Y%m%d`
fi


CURDIR=`cd $(dirname $0);pwd`

mainjob $dstr>/tmp/tele.message

docker run \
 --env-file $HOME/.self_env \
 -v /tmp/tele.message:/tmp/tele.message \
 -v $CURDIR/send_telegram.py:/send_telegram.py \
 --rm -i \
 tknpoon/private:c01telegram \
 python /send_telegram.py < /tmp/tele.message
 
sleep 1

rm -f /tmp/tele.message 2>/dev/null

