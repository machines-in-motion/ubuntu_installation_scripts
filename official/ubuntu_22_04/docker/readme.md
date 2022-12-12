# Use docker in a nutshell

## Build the docker images

"cd" to the folder of this readme.txt

```bash
cd ubunu_installation_scripts/official/ubuntu_18_04/docker/core
docker build -t docker.is.localnet:5000/amd/18.04:core .

cd ubunu_installation_scripts/official/ubuntu_18_04/docker/ros
docker build -t docker.is.localnet:5000/amd/18.04:ros .

cd ubunu_installation_scripts/official/ubuntu_18_04/docker/laas
docker build -t docker.is.localnet:5000/amd/18.04:laas .

cd ubunu_installation_scripts/official/ubuntu_18_04/docker/code
docker build -t docker.is.localnet:5000/amd/18.04:code .
```

## Run your docker

In order to launch a bash terminal in a docker container with a shared folder

```bash
docker run --rm -it -v <path local machine>:/tmp docker.is.localnet:5000/amd/18.04:code /bin/bash
```

- --rm  : option will delete the container after used (avoid too much memory used)
- -i    : Keep STDIN open even if not attached
- -t    : Allocate a pseudo-tty
- -v    : Allow to share a folder from your machine to the docker container => <path in your machine>:<path in the container>
- "docker.is.localnet:5000/amd/official:18.04"  : is the name of the image to run
- /bin/bash is the executable to run

# Exporting the image to portus (MPI-IS server)

First of all this is automatically done by the continuous integration system upon
any modification of this git repository.

If you want to update the image manually please follow the following procedure:

## Procedure to login and export to portus

1. create a file /etc/docker/daemon.json and add to it:

```
{
    "insecure-registries": [ "docker.is.localnet:5000" ]
}
```

2. restart docker:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

3. login to portus

```bash
docker login https://docker.is.localnet:5000
```

4. build

cf above

5. push

```bash
docker push docker.is.localnet:5000/amd/18.04:code
```

# RAI in the docker file...

For being able to download RAI, docker must be configured with the DNS IP (to understand code.is.localnet).

configuration of docker, from https://stackoverflow.com/questions/25130536/dockerfile-docker-build-cant-download-packages-centos-yum-debian-ubuntu-ap :

1) to get DNS IP:

```bash
nmcli dev list iface eth0
```

2) edit : /etc/defaults/docker (DOCKER_OPTS)
