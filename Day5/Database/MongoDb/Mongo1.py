import pymongo
"""  list_collection_names() like table in sql"""
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydbtest"]
collist=mydb.list_collection_names()
if "custormers" in collist:
     
    print "collection exists"
else:
    print "error"
