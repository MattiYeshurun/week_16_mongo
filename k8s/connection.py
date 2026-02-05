from pymongo import MongoClient

client = MongoClient('mongodb://root:root123@localhost:27017/')
database = client["testdb"]
collection = database["testcollection"]

