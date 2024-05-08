import os
import sys
from scr.exeption import CustomException
from scr.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

# dataclasses module is used to create data classes. which are used to store the data and the configuration and pass it to the other classes and functions and methods and also used to store the data in the form of objects.

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # The data_path variable is used to store the path of the data file.
    test_data_path: str= os.path.join("artifacts","test.csv")
    train_data_path: str= os.path.join("artifacts","train.csv")
    training_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.Ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion initiated")
        try:
            df=pd.read_csv("notebook\stud.csv")

            #os.makedirs() method is used to create a directory named artifact in the current working directory. and store the data in the artifact folder
            os.makedirs(os.path.dirname(self.Ingestion_config.training_data_path),exist_ok=True)
            logging.info("Data stored in the artifact folder")
            df.to_csv(self.Ingestion_config.training_data_path,index=False,header=True)

            

            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.Ingestion_config.train_data_path,index=False,header=True)

            test_data.to_csv(self.Ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data split successful")
            logging.info("test and train data stored in the artifact folder")

        except Exception as e:
            raise CustomException(e,sys)
        

if "__main__"==__name__:
    obj = DataIngestion()
    obj.initiate_data_ingestion()
