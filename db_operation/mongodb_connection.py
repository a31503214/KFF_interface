from pymongo import MongoClient

conn = MongoClient("localhost",27017)
db = conn.testdb
db.col.insert({"name":"Lily","city":"hangzhou","age":25})
db.col.find_one()