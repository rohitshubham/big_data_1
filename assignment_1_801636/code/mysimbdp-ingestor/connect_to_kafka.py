from kafka import KafkaProducer
import time

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

for i in range(10000000):
    time.sleep(0.5)
    text = "Hello World "+ str(i)
    ack = producer.send(topicName, str.encode(text)) 
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)