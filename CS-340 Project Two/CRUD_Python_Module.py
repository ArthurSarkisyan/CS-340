# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

               
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("An error occurred while inserting the document:", e)
                return False
        else:
            return False

    # Complete this read method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print("An error occurred while reading the documents:", e)
                return []
        else:
            return []
        
        
        
            # Complete this update method to implement the U in CRUD.
    def update(self, query, data):
        if query is not None and data is not None:
            try:
                result = self.collection.update_many(query, {"$set": data})
                return result.modified_count
            except Exception as e:
                print("An error occurred while updating the documents:", e)
                return 0
        else:
            return 0
        
        
        
            # Complete this delete method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("An error occurred while deleting the documents:", e)
                return 0
        else:
            return 0