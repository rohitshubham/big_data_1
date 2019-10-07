#!/binb/bash

sudo docker run -d --name=dev-consul --net=host -e CONSUL_BIND_INTERFACE=eth0 consul

#gliderLabs/registrator adds the service discovery using Consul
sudo docker run -d --name=registrator --net=host --volume=/var/run/docker.sock:/tmp/docker.sock gliderlabs/registrator:latest consul://localhost:8500