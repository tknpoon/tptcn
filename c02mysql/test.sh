#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

stmt="
SELECT s1.symbol, s1.date, s1.Price
FROM
  tHKEX_Sales s1
  JOIN (SELECT symbol, Date, MIN(Serial) as Serial
        FROM tHKEX_Sales
        WHERE tHKEX_Sales.Flag NOT IN ('P','M','D','C')
        GROUP BY symbol, Date
  ) s2
ON s1.symbol = s2.symbol
 AND s1.Date = s2.Date
 AND s1.Serial = s2.Serial
"

echo "$stmt" | \
docker exec -i \
  $CONTAINER_NAME \
  bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
