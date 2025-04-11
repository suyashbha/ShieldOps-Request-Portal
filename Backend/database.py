from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Loading the environment variables from our .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "ProjectDB"

def get_db_client():

    client = AsyncIOMotorClient(
        MONGO_URI,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db = client[DATABASE_NAME]
    return db
