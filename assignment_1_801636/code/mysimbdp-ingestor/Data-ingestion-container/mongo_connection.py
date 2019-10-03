import pymongo

# kafka connection strings
#Strictly internal APIs to call and save data in MongoDB Container
__connectionString = "mongodb://localhost:27017"
__databaseName = "mysimbdp-coredms"

def __connectToDatabase(collectionName):
    simpbdp_client = pymongo.MongoClient(__connectionString)
    getDatabase = simpbdp_client[__databaseName]
    return getDatabase[collectionName] 


def connectAndInsertRow(valueToBeStored, collectionName = "airbnb"):
    current_collection = __connectToDatabase(collectionName)
    current_collection.insert_one(valueToBeStored)

