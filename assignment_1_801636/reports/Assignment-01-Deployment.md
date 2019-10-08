# Deployment 1

### CS-E4640 Big data platforms 
#### Rohit Raj - 801636
---

This assignment has 4 components that we need to deploy:
1. Mysimbdp-coredms
2. Mysimbdp-ingestor
3. Mysimbdp-daas
4. Consul for service discovery


We will deploy the assignment in the same serial as above. Also, you will need root access to install components and run docker.


## 1.Mysimbdp-coredms

To deploy the sharded instance of MongoDB, use the following steps:

1. Install `docker` and `docker-compose` using the script `/code/scripts/install_docker.sh`
2. Run the script `/code/scripts/python-dependencies.sh`
2. Run the script `/code/scripts/install_mongo_container.sh`. This will automatically pull, install, enable replication and shard the database named `mysimbdp-coredms` and run all the 10 containers.  

To access the terminal interface of our sharded mongoDB use the command:
```bash
sudo docker-compose exec -i router mongo 
```

To check the status of sharding use 
> sh.status()

in the terminal.

To stop the database, just use 
```bash
sudo docker-compose stop
```
---
## 2. Mysimbdp-ingestor

To start our mysimbdp-ingestor, we need to follow the following steps:

1. Run the script `/code/scripts/DockerBuild Configs/KafkaDockerContainers/install_kafka_confluent.sh`. This will start our Kafka message broker.
2. Run the script `/code/scripts/DockerBuild Configs/DataIngestorApi's/data_ingestor_start.sh`. This will build and then run the Python ingestor middleware container and will automatically connect the Kafka and MongoDB.

To access the UI of Kafka, go to `localhost:9021`.

--- 

## 3. Mysimbdp-daas

To start the simple-daas:

1. Run the script `/code/scripts/DockerBuild Configs/simbdp-daasApis/simbdp-daasApis_start.sh`. It will build the `docker` container, and start the script.

The Daas server runs on port `5000`. You can use Postman or similar service to hit the Rest APIs.

## 4. Consul for service discovery

To start the Consul:
1. Run the script `/code/scripts/mysimbdp-coredms-servicediscovery/install_consul.sh`

This will install and run consul as well as `Registrator` plugin for consul. Registrator will automatically register the MongoDb instances, Kafka broker to the Consul and we don't need to do anything.

To see the UI of Consul, go to `localhost:8500/ui`.

To manually add a service from file(as asked in one of the questions), `/code/scripts/mysimbdp-coredms-servicediscovery/consul_add_service_manually.sh`. The filename is `payload.json`.

---

Note: To start insertion of data from `/data/data.csv`, into the Kafka ingestion queue, run the python script:
```bash
python3 /code/mysimbdp-ingestor/connect_to_kafka.py
```
no container is required for this script.