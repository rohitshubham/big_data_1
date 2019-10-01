from kafka import KafkaProducer
import csv
import time

bootstrap_servers = ['localhost:9092']
topicName = 'mysimbdp'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()


with open("../../data/data.csv") as file: 
    data = file.read()
    dataRow = data.splitlines()
    for idx, i in enumerate(dataRow):
        time.sleep(0.5)
        ack = producer.send(topicName, str.encode(i))
        metadata = ack.get()
        print("Published row " + str(idx) + ".")

