from Network_Security.constants import Training_pipeline
from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.Exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.Entity.config_entity import DataIngestonConfig, trainigPipelineConfig
import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = trainigPipelineConfig()
        data_ingestion_config = DataIngestonConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiating Data Ingestion...")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
