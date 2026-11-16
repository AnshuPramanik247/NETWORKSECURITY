import os
import sys
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from Network_Security.Exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

# Load environment variables from .env
load_dotenv()

uri = os.getenv("MONGO_DB_URL")
ca = certifi.where()

if not uri:
    raise ValueError("MONGO_DB_URL is not set in the .env file.")

try:
    client = MongoClient(uri, tlsCAFile=ca)
    client.admin.command("ping")
    print("Connected successfully to MongoDB Atlas!")
    client.close()

except Exception as e:
    raise NetworkSecurityException(e, sys)
