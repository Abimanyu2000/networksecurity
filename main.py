import sys

from networksecurity.entity.config_entity import TrainPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__=="__main__":
    try:
        trainpipelineconfig=TrainPipelineConfig()
        data_ingestionconfig=DataIngestionConfig(trainpipelineconfig)
        data_ingestion=DataIngestion(data_ingestionconfig)
        logging.info("Initiated the data ingestion")

        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

        logging.info("Data ingestion completed")

        data_validation_config=DataValidationConfig(trainpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Initiated the data validation")

        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")

        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)