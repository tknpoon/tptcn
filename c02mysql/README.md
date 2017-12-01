#
cd ~/tptcn/c02mysql

bash ~/tptcn/c02mysql/run-mysql.sh
docker exec -it c02mysql mysql -uroot -p

bash ~/tptcn/c02mysql/run-myadmin.sh
