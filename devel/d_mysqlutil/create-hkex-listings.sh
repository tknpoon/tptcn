#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

STAGE=${TAG_NAME:0:1}

stmt="
CREATE TABLE IF NOT EXISTS \`${STAGE}_hkex_listings\` (
\`ID\` int(11) NOT NULL AUTO_INCREMENT,
\`symbol\` VARCHAR(10) COLLATE utf8_unicode_ci NOT NULL,
\`eName\` VARCHAR(30) COLLATE utf8_unicode_ci DEFAULT NULL,
\`cName\` VARCHAR(30) COLLATE utf8_unicode_ci DEFAULT NULL,
\`lotSize\` int(11) DEFAULT NULL,
PRIMARY KEY (\`ID\`),
UNIQUE KEY \`Symbol\` (\`symbol\`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
"

echo "$stmt" | \
docker exec -i \
  g_mysql \
  bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
