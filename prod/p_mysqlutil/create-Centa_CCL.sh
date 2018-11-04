#!/bin/bash

DIRNAME=`dirname $0`
TAG_NAME=$(cd $DIRNAME ; basename `pwd`)

STAGE=${TAG_NAME:0:1}

THE_DB=${STAGE}_master

stmt="
USE ${THE_DB};
CREATE TABLE IF NOT EXISTS \`Centa_CCL\` (
\`ID\` int(11) NOT NULL AUTO_INCREMENT,
\`FromDate\` date NOT NULL,
\`ToDate\` date NOT NULL,
\`CCL_HK\` float DEFAULT NULL,
\`CCL_KLN\` float DEFAULT NULL,
\`CCL_NTE\` float DEFAULT NULL,
\`CCL_NTW\` float DEFAULT NULL,
\`CCL_mass\` float DEFAULT NULL,
\`CCL_L\` float DEFAULT NULL,
\`CCL_SM\` float DEFAULT NULL,
\`CCL\` float DEFAULT NULL,
PRIMARY KEY (\`ID\`),
UNIQUE KEY \`FromDate\` (\`FromDate\`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Centanet Data'
"

echo "$stmt" | \
docker exec -i \
  g_mysql \
  bash -c 'exec mysql $MYSQL_DATABASE -u$MYSQL_USER -p"$MYSQL_PASSWORD"'
