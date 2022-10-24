from struct import pack
import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.TestPDB
collection = db.TestCol

with open('packets.txt') as file:
    for line in file:
        packet = json.loads(line)
        packet.pop('_id')
        collection.insert_one(packet)
