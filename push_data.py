from pymongo import MongoClient
import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
## Trusted certificates authorities
ca=certifi.where()

import pandas as pd
import numpy as np 
import pymongo
from Network_Security.Exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

class NetworkDataExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(str(data.T.to_json())).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongoclient = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.db = self.mongoclient[self.database]
            self.col = self.db[self.collection]
            self.col.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = 'Network_data/phisingData.csv'
    DATABASE = 'ANSHUAI'
    collection = 'Networkdata'
    networkobj = NetworkDataExtraction()
    records = networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, collection)
    print(no_of_records)