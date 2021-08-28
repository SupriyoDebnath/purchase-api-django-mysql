## _Reference_

- [MySQL Docker Image ](https://hub.docker.com/_/mysql)
- [Official Docker Network Setup Guide](https://docs.docker.com/network/)
- [Official Docker Volume Management Guide](https://docs.docker.com/storage/volumes/)

<br>

## _Pull Image_
```sh
docker pull mysql:latest
```

## _Check Image_
```sh
docker image ls -a | grep mysql
docker inspect mysql:latest
```

## _Create Network_
```sh
docker network create pm-net
```

## _Check Network_
```sh
docker network ls | grep pm-net
docker inspect pm-net
```

## _Create Volume_
```sh
docker volume create pm-db-data
```

## _Check Volume_
```sh
docker volume ls | grep pm-db-data
docker inspect pm-db-data
```

## _Run Container_
```sh
docker run -d \
  --name pm-db \
  -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
  --network pm-net \
  -p 3306:3306 \
  -p 33060:33060 \
  --mount type=volume,src=pm-db-data,dst=/var/lib/mysql \
  mysql:latest
```

## _Check Container `[look for GENERATED ROOT PASSWORD in container log]`_
```sh
docker container ls -a | grep pm-db
docker inspect pm-db
docker container logs pm-db
random root password = ishiuzei9uj5ceilohHoh6da5na7Tiov
docker exec -it pm-db sh
 > whoami
 > exit
```

## _Check MySQL Installation_
```sh
mysqlshow -u root -p
apt update
apt install procps
```

## _Create App User_
```sh
mysql -u root -p
 > CREATE USER 'pm-user'@'%' IDENTIFIED BY 'pmuser@2021';
 > GRANT ALL ON *.* TO 'pm-user'@'%' WITH GRANT OPTION;
 > SHOW GRANTS FOR 'pm-user'@'%';
 > quit
```