
# Login to portus

1. create a file /etc/docker/daemon.json and add to it:

{
    "insecure-registries": [ "docker.is.localnet:5000" ]
}

2. restart docker:

sudo systemctl daemon-reload
sudo systemctl restart docker

3. login to portus

docker login https://docker.is.localnet:5000

4. build

docker build -t docker.is.localnet:5000/amd/official:16.04 .

5. push

docker push docker.is.localnet:5000/amd/official:16.04


# RAI

For being able to download RAI, docker must be configured with the DNS IP (to understand code.is.localnet).

configuration of docker, from https://stackoverflow.com/questions/25130536/dockerfile-docker-build-cant-download-packages-centos-yum-debian-ubuntu-ap :

1) to get DNS IP:

nmcli dev list iface eth0

2) edit : /etc/defaults/docker (DOCKER_OPTS)
