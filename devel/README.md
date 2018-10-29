# devel

### Devel ports are in range of 2xxxx
| Container   | published | expose | image | description |
| :---------- | :-------: | :----: | :---------- | ---- |
| d_telegram  |  20025    |   25   | tknpoon/private:d_telegram | smtp to Telegram  | 
| d_xmysql  |  192.168.8.xx:23000    |   3000   | tknpoon/private:d_xmysql | Xmysql (mysql to REST API)  | 
| d_scrapy_cclhistory | --     |   -- |  vimagick/scrapyd | Scrapy for CCL history ; crontab to run weekly |
| d_phpmyadmin  |  20080    |   80   | phpmyadmin/phpmyadmin | php My Admin  | 
| d_ubuntu    |    --     |   --   | tknpoon/private:d_ubuntu | ubuntu 18.04 |
