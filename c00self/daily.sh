#!/bin/bash
scripts="c00self/grab.sh"
scripts="$scripts c11yahoo/run-grab_yahoo.sh"
scripts="$scripts c05scrapyd/run-scrapy-hkex-today.sh"
scripts="$scripts c00self/replace_sql.sh"
scripts="$scripts c00self/check.sh"

for s in $scripts
do 
 echo ==== working on.... /home/ubuntu/repo/tptcn/$s `date`
 /bin/bash /home/ubuntu/repo/tptcn/$s
done

