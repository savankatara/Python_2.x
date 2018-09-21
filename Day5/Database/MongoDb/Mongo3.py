import pymongo
"""  list_collection_names() like table in sql"""
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydbtest"]
mycol=mydb["custormers"] 
print mydb.list_collection_names()
