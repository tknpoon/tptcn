#

bash ~/tptcn/c02mysql/run-mysql.sh

docker exec -it c02mysql mysql -uroot -pMyNewPass "ALTER USER 'root'  IDENTIFIED BY 'xMyNewPassx';"

bash ~/tptcn/c02mysql/run-myadmin.sh
