from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template
from bson.json_util import loads, dumps
from kafka import KafkaProducer

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mysimbdp-coredms"
mongo = PyMongo(app)
airbnb_collection = mongo.db.airbnb

# API for connecting to kafka 
# The name of the server and topic on which we publish
bootstrap_servers = ['localhost:9092']
topicName = 'mysimbdp'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

@app.route("/")
def mainPage():
    return render_template("main.html")


@app.route("/user/<username>", methods=["GET"])
def user_profile(username):
    user = airbnb_collection.find_one_or_404({"host_name": username})
    return dumps(user)

@app.route("/getByHostId/<hostId>",  methods=["GET"])
def host_profile(hostId):
    host = airbnb_collection.find_one_or_404({"host_id": hostId})
    return dumps(host)

@app.route("/getByNeighbourhood/<neighbourhood>",  methods=["GET"])
def neighborhood(neighbourhood):
    neighborhood = airbnb_collection.find({"neighbourhood": neighbourhood})
    return dumps(neighborhood)

@app.route("/updateHostName/<hostID>/<newHostName>",  methods=["GET", "POST"])
def updateHostName(hostID, newHostName):
    result = airbnb_collection.update_one({"host_id": hostID}, {"$set" : {"host_name": newHostName}})
    return dumps(result.modified_count)

#Insertion API via Kafka
@app.route("/insertData/<data>",  methods=["POST"])
def insertData(data):
    ack = producer.send(topicName, str.encode(i))
    metadata = ack.get()
    return "inserted the data!"

if __name__ == "__main__":
    app.run(debug=True)
