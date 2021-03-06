#!/bin/bash

CONTAINER_NAME=c02mysql

CURDIR=`cd $(dirname $0); pwd`
VOLDIR=$HOME/vol/$CONTAINER_NAME

stmt="ALTER TABLE tHKEX_Quotation DROP Open "

stmt="
ALTER TABLE tHKEX_Quotation 
 CHANGE Name Name VARCHAR(25) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
 CHANGE PrevClose PrevClose DECIMAL(10,3) NULL DEFAULT NULL,
 CHANGE High High DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Low Low DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Close Close DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Bid Bid DECIMAL(10,3) NULL DEFAULT NULL, 
 CHANGE Ask Ask DECIMAL(10,3) NULL DEFAULT NULL;
"

stmt="ALTER TABLE tHKEX_Sales 
 CHANGE Serial Serial VARCHAR(7) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL, 
 CHANGE Price Price DECIMAL(10,3) NULL DEFAULT NULL;
"
stmt="
ALTER TABLE tHKEX_Sales
 CHANGE symbol symbol VARCHAR(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
 CHANGE Serial Serial VARCHAR(7) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
 CHANGE Flag Flag VARCHAR(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL;
"

stmt="
alter table tDailyPrice convert to character set utf8 collate utf8_unicode_ci;
alter table tSymbol convert to character set utf8 collate utf8_unicode_ci;
alter table tVendor convert to character set utf8 collate utf8_unicode_ci;
alter table tYAHOO_Daily convert to character set utf8 collate utf8_unicode_ci;
alter table tHKEX_Quotation convert to character set utf8 collate utf8_unicode_ci;
alter table tHKEX_Sales convert to character set utf8 collate utf8_unicode_ci;
"

echo "$stmt" | \
docker exec -i \
  $CONTAINER_NAME \
  bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
