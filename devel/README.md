# devel

### Devel ports are in range of 2xxxx
| Container   | image                     | published         | expose | description |
| :---------- | :------------------------ | :---------------: | :----: | ------------- |
| d_telegram  | tknpoon/private:d_telegram| 20025             |   25   | smtp to Telegram  | 
| d_scrapy_cclhistory |  vimagick/scrapyd | --                |   --   | Scrapy for CCL history weekly store to `d_xmysqlrw` |
| d_phpmyadmin | phpmyadmin/phpmyadmin    |  20080            |   80   | php My Admin to `g_mysql`  | 
| d_ubuntu     | tknpoon/private:d_ubuntu |    --             |   --   | ubuntu 18.04         |
