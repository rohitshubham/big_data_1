from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template
from bson.json_util import loads, dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mysimbdp-coredms"
mongo = PyMongo(app)
airbnb_collection = mongo.db.airbnb


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
def neighbourhood(neighbourhood):
    neighbourhood = airbnb_collection.find({"neighbourhood": neighbourhood})
    return dumps(neighbourhood)

@app.route("/updateHostName/<hostID>/<newHostName>",  methods=["GET", "POST"])
def updateHostName(hostID, newHostName):
    result = airbnb_collection.update_one({"host_id": hostID}, {"$set" : {"host_name": newHostName}})
    return dumps(result.modified_count)

if __name__ == "__main__":
    app.run(debug=True)
