from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
        
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:50358/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            print('Nothing to save, because data parameter is empty')
            return False
            
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data)
        else:
            print('Nothing to read, because data parameter is empty')
            return False

    def update(self, data, change):
        if data is not None:
            return self.database.animals.update(data,{ "$set": change})
        else:
            print('Nothing to update, because data parameter is empty')
            return False

    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)
        else:
            print('Nothing to delete, because data parameter is empty')
            return False