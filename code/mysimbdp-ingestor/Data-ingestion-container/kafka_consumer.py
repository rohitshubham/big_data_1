from kafka import KafkaConsumer
import sys
from mongo_connection import connectAndInsertRow

bootstrap_servers = ['localhost:9092']
topicName = 'mysimbdp'

print("Starting to listen for messages on topic : " + topicName + ". ")    

consumer = KafkaConsumer(topicName, group_id = 'myGroup',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')

print("Successfully connected to kafka consumer process!")

def getFormattedData(message):
    data = message.split(",")
    myDict = {  "id" : data[0],
                "name" : data[1],
                "host_id" : data[2],
                "host_name" : data[3],
                "neighbourhood_group" : data[4],
                "neighbourhood" : data[5],
                "latitude" : data[6],
                "longitude" : data[7],
                "room_type" : data[8],
                "price" : data[9],
                "minimum_nights" : data[10],
                "number_of_reviews": data[11],
                "last_review" : data[12],
                "reviews_per_month" : data[13],
                "calculated_host_listings_count" : data[14],
                "availability_365": data[15]
                }
    return myDict



try:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        formattedData = getFormattedData(str(message.value))
        connectAndInsertRow(formattedData)        
except Exception:
    pass
	
