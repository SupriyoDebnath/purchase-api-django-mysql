## _Reference_

- [Official Docker Installation Guide for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Official Docker Machine Installation Guide](https://docs.docker.com/machine/install-machine/)
- [Official Releases for Docker Machine](https://github.com/docker/machine/releases)
- [Official Docker Compose Installation Guide](https://docs.docker.com/compose/install/)
- [Official Releases for Docker Compose](https://github.com/docker/machine/releases)

<br>

## _Remove older Docker Packages_
```sh
apt remove docker docker.io containerd runc
apt remove docker-engine
```

## _Install Docker using Convenience Script `[not recommended for Production]`_
```sh
curl -fsSL https://get.docker.com -o get-docker.sh
DRY_RUN=1 sh ./get-docker.sh
sh get-docker.sh
```

## _Configure Docker to start on Boot_
```sh
systemctl enable docker.service
systemctl enable containerd.service
```

## _Install Docker Machine_
```sh
curl -L https://github.com/docker/machine/releases/download/v0.16.2/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine
mv /tmp/docker-machine /usr/local/bin/docker-machine
chmod +x /usr/local/bin/docker-machine
```

## _Install Docker Compose_
```sh
curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

## _Check Installation_
```sh
docker version
docker run hello-world
docker-machine version
docker-compose version
```