from pymongo import MongoClient as mongoDB
import os
class database:
    def __init__(self):
        self.client1 = mongoDB(os.environ['host-0f-mongo1'], 27017)
    
    def getClient1(self):
        return self.client1
