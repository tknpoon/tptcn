#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

###############
#for y in 2018; do
#  for m in 12 ; do
#    docker exec -i g_mysql cat 

for y in {2014..2018} ; do
 for m in {1..12} ; do
  for d in {1..31} ; do
    date -d "$m/$d/$y">/dev/null 2>&1 && \
    docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD ${TAG_NAME:0:1}_master <<AAA
    UPDATE
      consolidated_daily AS dest,
      ( SELECT symbol, Date, (SUM(Price * Volume)/SUM(Volume)) AS VWAP
        FROM hkex_sales
        WHERE symbol IN (SELECT symbol FROM diary WHERE market='HK' )
          AND Date = '${y}-${m}-${d}' 
        GROUP BY symbol, Date
      ) AS src
    SET dest.VWAP = src.VWAP
    WHERE dest.symbol = src.symbol
      AND dest.Date = src.Date
    ;
    COMMIT;

    UPDATE
      consolidated_daily AS dest,
      ( SELECT symbol, Date, (SUM(Price * Volume)/SUM(Volume)) AS VWAP
        FROM hkex_sales
        WHERE symbol IN (SELECT symbol FROM diary WHERE market='HK' )
          AND Date = '${y}-${m}-${d}' 
          AND LEFT(Serial,1) = 'A'
        GROUP BY symbol, Date
      ) AS src
    SET dest.VWAPampre = src.VWAP
    WHERE dest.symbol = src.symbol
      AND dest.Date = src.Date
    ;
    COMMIT;

    UPDATE
      consolidated_daily AS dest,
      ( SELECT symbol, Date, (SUM(Price * Volume)/SUM(Volume)) AS VWAP
        FROM hkex_sales
        WHERE symbol IN (SELECT symbol FROM diary WHERE market='HK' )
          AND Date = '${y}-${m}-${d}' 
          AND LEFT(Serial,1) = 'M'
        GROUP BY symbol, Date
      ) AS src
    SET dest.VWAPam = src.VWAP
    WHERE dest.symbol = src.symbol
      AND dest.Date = src.Date
    ;
    COMMIT;

    UPDATE
      consolidated_daily AS dest,
      ( SELECT symbol, Date, (SUM(Price * Volume)/SUM(Volume)) AS VWAP
        FROM hkex_sales
        WHERE symbol IN (SELECT symbol FROM diary WHERE market='HK' )
          AND Date = '${y}-${m}-${d}' 
          AND LEFT(Serial,1) = 'P'
        GROUP BY symbol, Date
      ) AS src
    SET dest.VWAPpm = src.VWAP
    WHERE dest.symbol = src.symbol
      AND dest.Date = src.Date
    ;
    COMMIT;

    UPDATE
      consolidated_daily AS dest,
      ( SELECT symbol, Date, (SUM(Price * Volume)/SUM(Volume)) AS VWAP
        FROM hkex_sales
        WHERE symbol IN (SELECT symbol FROM diary WHERE market='HK' )
          AND Date = '${y}-${m}-${d}' 
          AND LEFT(Serial,1) = 'U'
        GROUP BY symbol, Date
      ) AS src
    SET dest.VWAPpmpost = src.VWAP
    WHERE dest.symbol = src.symbol
      AND dest.Date = src.Date
    ;
    COMMIT;
AAA
  done
 done
done