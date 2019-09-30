import pymongo

__connectionString = "mongodb://localhost:27017"
__databaseName = "mysimbdp-coredms"

def __connectToDatabase(collectionName):
    simpbdp_client = pymongo.MongoClient(__connectionString)
    getDatabase = simpbdp_client[__databaseName]
    return getDatabase[collectionName] 


def connectAndInsertRow(valueToBeStored, collectionName = "airbnb"):
    current_collection = __connectToDatabase(collectionName)
    mydict = {"name" : "rohitRaj", "address": "Highway37"}
    current_collection.insert_one(mydict)

# Each topic incoming from the message broker should ideally get inserted into a new collection
connectAndInsertRow({"name" : "john", "address": "Highway37"}, "customers")

