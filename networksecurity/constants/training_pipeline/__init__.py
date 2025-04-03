


"""
Defining all common constant variable for training pipeline
"""

PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "phisingData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"


TARGET_COLUMN:str = "Result"

"""
Data ingestion related constants
"""
DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str ="SAMPLE"
DATA_INGESTION_DIR:str = "data-ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTED_DIR:str =  "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

