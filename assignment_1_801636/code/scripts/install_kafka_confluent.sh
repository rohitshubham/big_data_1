#!/bin/sh
set -e

#Installation of confluent's kafka wrapper
sudo docker-compose up -d --build

#To stop it
#sudo docker container stop $(sudo docker container ls -a -q -f "label=io.confluent.docker")
# Serves the admin panel at http://localhost:9021/
