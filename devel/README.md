# devel

### Devel ports are in range of 2xxxx
| Container   | image                     | published         | expose | description |
| :---------- | :------------------------ | :---------------: | :----: | ------------- |
| d_telegram  | tknpoon/private:d_telegram| 20025             |   25   | smtp to Telegram  | 
| d_xmysql    | tknpoon/private:d_xmysql  | 192.168.8.xx:23000|   3000 | Xmysql (mysql to REST API)  | 
| d_scrapy_cclhistory |  vimagick/scrapyd | --                |   --   | Scrapy for CCL history ; crontab to run weekly |
| d_phpmyadmin | phpmyadmin/phpmyadmin    |  20080            |   80   | php My Admin         | 
| d_ubuntu     | tknpoon/private:d_ubuntu |    --             |   --   | ubuntu 18.04         |
