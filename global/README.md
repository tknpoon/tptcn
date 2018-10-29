# global

### Devel ports are in range of 5xxxx
| Container   | image     | published   | expose | description |
| :---------- | :-------  | :---------: | :----: | ------------- |
| g_mysql     | mysql:5.7 | 53306       |   3306 | MySql   | 

```
for d in `docker ps --filter 'name=_xmysql' --format '{{.Names}}'`; do
 docker kill $d
 `find /home/ubuntu/repo/tptcn -name d_xmysql`/run.sh
done
```
