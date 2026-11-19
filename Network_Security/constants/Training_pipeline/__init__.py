import os
import sys
import numpy as np
import pandas as pd


# Define common constant variiable for traning pipeline

TARGET_COLUMN='Result'
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = 'Artifacts'
FILE_NAME: str = 'phisingData.csv'

TRAIN_FILE_NAME: str = 'Train.csv'
TEST_FILE_NAME:str = 'Test.csv'
# Data Ingeston related constant start with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME:str = 'Networkdata'
DATA_INGESTION_DATABASE_NAME:str = 'ANSHUAI'
DATA_INGESTION_DIR_NAME:str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR:str = 'ingesteed'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2