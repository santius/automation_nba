from pymongo import MongoClient
from bson.objectid import ObjectId

class DBHelper():

    def getFirstPlace(host,port, database):
        client = MongoClient(host,port)
        db = client.database
        return db.teams.find_one().get(name)