#!/bin/bash
set -a 
. $HOME/.self_env
DIRNAME=`cd $(dirname $0); pwd`
CURDIR=`cd $(dirname $0); pwd`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

###############
sql='
INSERT INTO `consolidated_daily` (symbol,Date,Open,High,Low,Close,Volume,Turnover,ShortVolume,ShortTurnover)
  SELECT
    s.symbol,
    q.Date as Date,
    IF(q.PrevClose > q.High, q.High, IF(q.PrevClose < q.Low, q.Low, q.PrevClose)) as Open,
    q.High as High,
    q.Low as Low,
    q.Close as Close,
    q.Volume as Volume,
    q.Turnover as Turnover,
    q.ShortVolume as ShortVolume,
    q.ShortTurnover as ShortTurnover
  FROM
    `hkex_quotation` q,
    (SELECT `symbol` FROM `diary` WHERE `market`="HK") s
  WHERE s.symbol = q.symbol
  ON DUPLICATE KEY UPDATE 
    Open=IF(q.PrevClose > q.High, q.High, IF(q.PrevClose < q.Low, q.Low, q.PrevClose)),
    High=q.High,
    Low=q.Low,
    Close=q.Close,
    Volume=q.Volume,
    Turnover=q.Turnover ,
    ShortVolume=q.ShortVolume,
    ShortTurnover=q.ShortTurnover 
;

UPDATE
  consolidated_daily dest,
  (
    SELECT
      tmeta.symbol,
      topen.Date as Date,
      topen.Price as Open
    FROM
      (
        SELECT s1.symbol, s1.date, s1.Price
        FROM
          hkex_sales s1
          JOIN (
            SELECT diary.symbol AS symbol, hkex_sales.Date AS Date, MIN(hkex_sales.Serial) AS Serial
            FROM
              diary, hkex_sales
            WHERE diary.symbol = hkex_sales.symbol
              AND hkex_sales.Flag NOT IN( 'P' , 'X')
            GROUP BY symbol, Date
          ) s2
          ON s1.symbol = s2.symbol
          AND s1.Date = s2.Date
          AND s1.Serial = s2.Serial
      ) topen,
      (
        SELECT
          symbol
        FROM diary
        WHERE 1
          AND market="HK"
      ) tmeta
    WHERE 1
      AND topen.symbol = tmeta.symbol
  ) src
SET dest.Open = src.Open
WHERE dest.symbol = src.symbol
  AND dest.Date = src.Date
;

'
###############
echo $sql | docker exec -i g_mysql mysql -u$MYSQL_USER -p$MYSQL_PASSWORD ${TAG_NAME:0:1}_master
