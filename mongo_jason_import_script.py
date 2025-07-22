import json
from pymongo import MongoClient

# Connect to MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")

# Create/use a database and collection
db = client["cool1"]
collection = db["people"]

# Load JSON data from file
#with open("data.json") as f:
with open(r"C:\Users\Michael\Downloads\test_db.users2.json") as f:
    data = json.load(f)

# Insert data into MongoDB
if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Data imported successfully!")
