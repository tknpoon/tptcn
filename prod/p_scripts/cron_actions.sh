#!/bin/bash
### run at xx20 and xx50
set -a 
. $HOME/.self_env

HHMM=$(date +%H%M)

#####
if [ "$HHMM" == "0020" ]; then
    c=$(docker ps -a -q --filter="name=p_telegram")
    [ "$c" = "" ] && $HOME/repo/tptcn/prod/p_telegram/run.sh
    
    c=$(docker ps -a -q --filter="name=g_mysql")
    [ "$c" = "" ] && $HOME/repo/tptcn/global/g_mysql/run.sh
fi
##### Daily @ 11:50
if [ "$HHMM" == "1150" -a "$(date +%w)" -ge 1 -a "$(date +%w)" -le 5 ]; then
    cd $HOME/repo/tptcn
    cd prod
    p_scripts/grabHK_1150.sh
    p_scrapy_hkab/runc.sh
    p_scripts/check_1150.sh
fi
##### Daily @ 21:20
if [ "$HHMM" == "2120" -a "$(date +%w)" -ge 1 -a "$(date +%w)" -le 5 ]; then
    cd $HOME/repo/tptcn
    cd prod
    p_scripts/grabHK_2115.sh
    p_scrapy_hkab/runc.sh
    p_scrapy_hkma/runc.sh
    p_scrapy_hkex/runc.sh
    p_scripts/consolidate_hk.sh
    p_scripts/cal_vwap.sh
    p_scripts/parse_stko.sh
    p_scripts/parse_hsio.sh
    p_scripts/parse_hhio.sh
    p_scripts/cal_rsi.sh
    p_scripts/cal_atr.sh
    p_scripts/check_2115.sh
fi
##### CCL @ Fri
if [ "$HHMM" == "1220" -a "$(date +%w)" -eq 5 ]; then
    cd $HOME/repo/tptcn
    cd prod
    p_scrapy_ccl/runc.sh
    p_scripts/check_ccl.sh
fi
