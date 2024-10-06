import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd

@dataclass
class DataIngestionConfig:
    train_data_split: str = os.path.join('artifacts', 'train.csv')
    test_data_split: str = os.path.join('artifacts', 'test.csv')
    raw_data_split: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('C:\\Users\\Anuruddh Bajpai\\Desktop\\sem5\\MachineLearningProjects\\Day3_ML_Project\\notebook\\data\\study_performance.csv')
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_split), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_split, index=False, header=True)
            logging.info("Train-test split initiated")

            # Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_split, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_split, index=False, header=True)

            logging.info("Ingestion of the data is completed")
            return self.ingestion_config.train_data_split, self.ingestion_config.test_data_split

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
