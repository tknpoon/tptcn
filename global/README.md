# global

### Devel ports are in range of 5xxxx
| Container   | image     | published   | expose | description |
| :---------- | :-------  | :---------: | :----: | ------------- |
| g_mysql     | mysql:5.7 | 53306       |   3306 | MySql   | 

#### Need restart the Xmysql containers
```
for d in `docker ps --filter 'name=_xmysql' --format '{{.Names}}'`; do
 docker kill $d
 sleep 3
 `find /home/ubuntu/repo/tptcn -name $d`/run.sh
done
```
#### OR start them if not started yet
```
for d in `find /home/ubuntu/repo/tptcn -name \*_xmysql\*`; do
 $d/run.sh
done
```
