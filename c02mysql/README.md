#

bash ~/tptcn/c02mysql/run-mysql.sh

docker exec -it c02mysql mysql -uroot -puseItOnce "ALTER USER 'root'  IDENTIFIED BY 'xMyNewPassx';"

bash ~/tptcn/c02mysql/run-myadmin.sh
