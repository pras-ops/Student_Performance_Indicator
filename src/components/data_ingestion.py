import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

'''
@dataclass: This is a decorator provided by the dataclass module in Python. It simplifies the process of creating classes that are primarily used to store data. It automatically generates boilerplate code, such as __init__() and __repr__() methods, based on the class attributes.

train_data_path, test_data_path, and raw_data_path: These are three attributes of the DataIngestionConfig class. Each attribute represents a file path related to data ingestion. The attribute type is specified as a string (str).

os.path.join('artifacts', "train.csv"): This is a function call that uses the os.path.join() method to concatenate the two provided strings, 'artifacts' and 'train.csv', into a single file path. Similarly, this is done for the test_data_path and raw_data_path attributes as well.
'''

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        '''class DataIngestion:: This line declares a class named DataIngestion. A class is a blueprint for creating objects that have certain properties (attributes) and behaviors (methods).

def __init__(self):: This is a special method called the constructor. It is executed automatically when an object of the class is created. The __init__ method initializes the object and sets up its initial state.

self.ingestion_config=DataIngestionConfig(): Within the constructor, this line creates an instance variable called ingestion_config and assigns it an object of the DataIngestionConfig class. This means that each DataIngestion object will have its own ingestion_config object to store configuration data.

DataIngestionConfig(): This part creates an instance of the DataIngestionConfig class. It calls the constructor of DataIngestionConfig to create a new object that represents the configuration for data ingestion.'''

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r"C:\Users\pj\Downloads\Student_Performance_Indicator\notebook\data\stud.csv")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
        '''
        logging.info("Entered the data ingestion method or component"): This line logs an informational message indicating that the data ingestion process has started.

try: and except Exception as e:: This code block is used for exception handling. It attempts to execute the code within the try block and if any exceptions occur, it captures the exception and raises a CustomException with the original exception and the sys module.

df=pd.read_csv('notebook\data\stud.csv'): This line reads a CSV file named 'stud.csv' and loads it into a pandas DataFrame object called df. The file is assumed to be located in the 'notebook\data' directory.

os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True): This line creates the directory structure specified by self.ingestion_config.train_data_path if it doesn't already exist. It ensures that the directory where the training data will be stored is created.

df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True): This line saves the DataFrame df as a CSV file using the file path specified by self.ingestion_config.raw_data_path. It writes the data without including the index and with a header.

train_set,test_set=train_test_split(df,test_size=0.2,random_state=42): This line splits the DataFrame df into training and testing datasets using the train_test_split function. The training dataset will be assigned to train_set, and the testing dataset will be assigned to test_set. The split ratio is set to 0.2, meaning 20% of the data will be used for testing, and the random_state parameter ensures reproducibility of the split.

train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True): This line saves the training dataset as a CSV file using the file path specified by self.ingestion_config.train_data_path. It writes the data without including the index and with a header.

test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True): This line saves the testing dataset as a CSV file using the file path specified by self.ingestion_config.test_data_path. It writes the data without including the index and with a header.

logging.info("Ingestion of the data is completed"): This line logs an informational message indicating that the data ingestion process has been completed.

return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path): This line returns a tuple containing the paths to the training and testing CSV files that were generated during the data ingestion process.
        '''
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

   

'''
if __name__=="__main__": checks if the script is being run directly as the main program.

obj=DataIngestion(): Creates an instance of the DataIngestion class by calling its constructor and assigns it to the variable obj.

train_data, test_data = obj.initiate_data_ingestion(): Calls the initiate_data_ingestion method of the DataIngestion class on the obj instance. This method performs data ingestion operations, such as reading data from a file, splitting it into train and test sets, and saving the data into separate files. The returned values, the paths to the train and test data files, are assigned to the variables train_data and test_data.

data_transformation=DataTransformation(): Creates an instance of the DataTransformation class and assigns it to the variable data_transformation.

train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data): Calls the initiate_data_transformation method of the DataTransformation class on the data_transformation instance. This method performs data transformation operations on the train and test data, such as preprocessing, feature engineering, or scaling. The transformed data arrays are returned and assigned to the variables train_arr and test_arr. The underscore _ indicates that the third returned value (if any) is being ignored.

modeltrainer=ModelTrainer(): Creates an instance of the ModelTrainer class and assigns it to the variable modeltrainer.

print(modeltrainer.initiate_model_trainer(train_arr, test_arr)): Calls the initiate_model_trainer method of the ModelTrainer class on the modeltrainer instance. This method performs model training operations using the provided train and test data arrays. The result of the training process is printed to the console.
'''