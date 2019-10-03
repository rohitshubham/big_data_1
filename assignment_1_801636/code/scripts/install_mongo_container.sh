## Builds, Installs a 3 shard MongoDB cluster with a replica of 2 for each shard
## There are 3 config servers for the metadata and this script automatically enables sharding for a database named mysimbdp-coredms
#!/bin/sh
set -e

#pulling the mongodb docker image
sudo docker pull mongo

#run the docker-compose image
sudo docker-compose up -f ../mysimbdp-coredms/mongo_sharded_docker/docker-compose.yml -d

#run the first init.sh script
sudo bash ../mysimbdp-coredms/mongo_sharded_docker/init.sh

# check if the instance has been started
sudo docker ps

#enable sharding on the database name
sudo docker-compose exec router mongo --eval "sh.enableSharding('mysimbdp-coredms')"