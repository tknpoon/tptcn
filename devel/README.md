# devel

### Devel ports are in range of 2xxxx
| Container   | image                     | published         | expose | description |
| :---------- | :------------------------ | :---------------: | :----: | ------------- |
| d_telegram  | tknpoon/private:d_telegram| 20025             |   25   | smtp to Telegram  | 
| d_xmysql    | tknpoon/private:d_xmysql  | 192.168.8.xx:23000|   3000 | Xmysql RO to `g_mysql`   | 
| d_xmysqlrw  | tknpoon/private:d_xmysqlrw| 192.168.8.xx:23001|   3000 | Xmysql RW to `g_mysql` | 
| d_scrapy_cclhistory |  vimagick/scrapyd | --                |   --   | Scrapy for CCL history weekly store to `g_mysql` |
| d_phpmyadmin | phpmyadmin/phpmyadmin    |  20080            |   80   | php My Admin to `g_mysql`  | 
| d_ubuntu     | tknpoon/private:d_ubuntu |    --             |   --   | ubuntu 18.04         |
