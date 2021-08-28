## _Reference_

- [Official Docker Image Build Guide](https://docs.docker.com/engine/reference/commandline/image_build/)

<br>

## _Build Image_
```sh
docker image build -t pm-app-image:1.1.0 .
```

## _Check Image_
```sh
docker image ls -a | grep pm-app-image
docker inspect pm-app-image:1.1.0
```

## _Create Volume_
```sh
docker volume create pm-app-media
```

## _Check Volume_
```sh
docker volume ls | grep pm-app-media
docker inspect pm-app-media
```

## _Run Container_
```sh
docker run -d \
  --name pm-app-mysql \
  --network pm-net \
  -p 8000:8000 \
  --mount type=volume,src=pm-app-media,dst=/workspace/source/media \
  pm-app-image:1.1.0
```

## _Check Container_
```sh
docker container ls -a | grep pm-app-mysql
docker inspect pm-app-mysql
docker container logs pm-app-mysql
docker exec -it pm-app-mysql sh
 > whoami
 > python3 manage.py migrate
 > python3 manage.py createsuperuser
 > exit