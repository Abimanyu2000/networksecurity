import sys

from networksecurity.entity.config_entity import TrainPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__=="__main__":
    try:
        trainpipelineconfig=TrainPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiated the data ingestion")

        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)