##Please note: This file is not a part of any container as this mimics the data being streamed to our kafka from external
## sources and as such, we assume this is NOT a part of our BDP and external data source
from kafka import KafkaProducer
import csv
import time

# The name of the server and topic on which we publish
bootstrap_servers = ['localhost:9092']
topicName = 'mysimbdp'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

# Reads data from the sourse CSV and calls the API for pushin the data to kafka
# by default this is pushed to a partition chosen by Kafka using round robin algo
with open("../../data/data.csv") as file: 
    data = file.read()
    dataRow = data.splitlines()
    for idx, i in enumerate(dataRow):
        time.sleep(0.1)
        ack = producer.send(topicName, str.encode(i))
        metadata = ack.get()
        print("Published row " + str(idx) + ".")

