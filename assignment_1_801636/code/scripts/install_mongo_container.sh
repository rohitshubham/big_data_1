#!/bin/sh
set -e

#pulling the mongodb docker image
sudo docker pull mongo

#run the image
# map the port and mount the volume to /usr/share directory
sudo docker run --name my-mongo -d -v /usr/share/mongodb:/data/db -p 27017:27017 mongo

# check if the instance has been started
sudo docker ps