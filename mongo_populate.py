from pymongo import MongoClient
from faker import Faker
import random

# Initialize Faker and MongoDB client
fake = Faker()
client = MongoClient("mongodb://localhost:27017/")  # Update if needed
db = client["test_db"]  # Your DB name
collection = db["users"]  # Your collection name

# Generate 1000 fake documents
documents = []
for _ in range(1000):
    doc = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "job": fake.job(),
        "company": fake.company(),
        "salary": round(random.uniform(30000, 150000), 2),
        "created_at": fake.iso8601()
    }
    documents.append(doc)

# Insert into MongoDB
collection.insert_many(documents)

print("✅ Inserted 1000 fake documents into MongoDB.")