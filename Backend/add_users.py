import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.hash import bcrypt
from dotenv import load_dotenv

# This is a sample code to add our agents/users to our database
# I have already created these users, but new users can be created using this script by changing the
# sample_users list

# Loading the environment variables from our .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = "ProjectDB"


client = AsyncIOMotorClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
db = client[DATABASE_NAME]
users_collection = db["users"]

async def add_sample_users():
    sample_users = [
        {
            "username": "agent.coulson",
            "password": bcrypt.hash("password123")
        },
        {
            "username": "agent.pepper",
            "password": bcrypt.hash("securepass456")
        },
        {
            "username": "agent.may",
            "password": bcrypt.hash("topsecret789")
        }
    ]

    for user in sample_users:
        existing_user = await users_collection.find_one({"username": user["username"]})
        if not existing_user:
            await users_collection.insert_one(user)
            print(f"User {user['username']} added successfully.")
        else:
            print(f"User {user['username']} already exists.")

if __name__ == "__main__":
    asyncio.run(add_sample_users())
