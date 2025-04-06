import sys

from networksecurity.entity.config_entity import TrainPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__=="__main__":
    try:
        ## train pipeline config initialised 
        trainpipelineconfig=TrainPipelineConfig()

        ### DATA INGESTION ###
        data_ingestionconfig=DataIngestionConfig(trainpipelineconfig)
        data_ingestion=DataIngestion(data_ingestionconfig)
        logging.info("Initiated the data ingestion")

        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

        logging.info("Data ingestion completed")

        ### DATA VALIDATION ###
        data_validation_config=DataValidationConfig(trainpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Initiated the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation completed")
        
        ### DATA TRANSFORMATION ###
        data_transformation_config = DataTransformationConfig(trainpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact
                           ,data_transformation_config=data_transformation_config)
        logging.info("Initiated data transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed")



    except Exception as e:
        raise NetworkSecurityException(e,sys)