import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

'''
import sys: This line imports the sys module, which provides access to some variables and functions related to the Python interpreter and its environment.

from dataclasses import dataclass: This line imports the dataclass decorator from the dataclasses module. The dataclass decorator is used to create classes with automatically generated special methods, such as __init__, __repr__, and __eq__, based on the defined class attributes.

import numpy as np: This line imports the numpy library and assigns it an alias np. numpy is a popular library for numerical computing in Python, providing efficient data structures and mathematical functions.

import pandas as pd: This line imports the pandas library and assigns it an alias pd. pandas is a powerful library for data manipulation and analysis, offering data structures like DataFrame and various data manipulation functions.

from sklearn.compose import ColumnTransformer: This line imports the ColumnTransformer class from the sklearn.compose module. ColumnTransformer is used for transforming specific columns of a dataset independently or as part of a machine learning pipeline.

from sklearn.impute import SimpleImputer: This line imports the SimpleImputer class from the sklearn.impute module. SimpleImputer is used to handle missing values by imputing them with a strategy like mean, median, or most frequent value.

from sklearn.pipeline import Pipeline: This line imports the Pipeline class from the sklearn.pipeline module. Pipeline is used to chain multiple data transformation steps together, providing a convenient way to organize and execute machine learning workflows.

from sklearn.preprocessing import OneHotEncoder, StandardScaler: This line imports the OneHotEncoder and StandardScaler classes from the sklearn.preprocessing module. OneHotEncoder is used for one-hot encoding categorical variables, and StandardScaler is used for standardizing numerical variables by subtracting the mean and scaling to unit variance.
'''

from src.exception import CustomException
from src.logger import logging
import os

'''
import os: This line imports the os module in Python. The os module provides functions for interacting with the operating system, such as working with files and directories.
'''

from src.utils import save_object

'''
from src.utils import save_object: This line imports the save_object function from a module called utils located in the src package. It assumes that there is a directory structure where the src directory contains a file or a package named utils.py or utils/__init__.py (to make it a package) that defines the save_object function.
'''

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

    '''
    @dataclass: This is a decorator in Python that automatically generates special methods, such as __init__ and __repr__, for the class based on its annotated fields. It simplifies the process of defining a class with properties.

class DataTransformationConfig:: This line starts the definition of the DataTransformationConfig class.

preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl"): This line declares a class attribute named preprocessor_obj_file_path and assigns it a value. The value is obtained by joining the strings 'artifacts' and 'preprocessor.pkl' using the os.path.join() function. This attribute represents the file path where the preprocessor object is stored.
    '''

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
        '''
        numerical_columns and categorical_columns: These variables store the names of numerical and categorical columns in the dataset, respectively.

num_pipeline: This is a pipeline for numerical data preprocessing. It consists of two steps: an imputer to fill missing values with the median, and a scaler to scale the numerical features using standardization.

cat_pipeline: This is a pipeline for categorical data preprocessing. It includes three steps: an imputer to fill missing values with the most frequent category, an one_hot_encoder to convert categorical variables into binary vectors, and a scaler to scale the categorical features using standardization.

preprocessor: This is a ColumnTransformer object that combines the numerical and categorical pipelines. It specifies how each column in the dataset should be transformed. Numerical columns are processed using the num_pipeline, while categorical columns are processed using the cat_pipeline.

Logging: The code includes logging statements to output the names of categorical and numerical columns for debugging purposes.

return preprocessor: The function returns the preprocessor object, which encapsulates the data transformation steps defined in the pipelines.
        '''
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        

        
    '''
    Reading Data: The code reads the training and testing datasets from the provided 
    
paths using pd.read_csv. These datasets are stored in the variables train_df and test_df.

Preprocessing Object: The code obtains a preprocessing object by calling the get_data_transformer_object method. This object will be used to transform the input features of the dataset.

Data Preparation: The code separates the input features and the target column from the training and testing datasets. The target column name is specified as "math_score", and the numerical columns are specified as ["writing_score", "reading_score"].

Applying Preprocessing: The code applies the preprocessing object on the input features of both the training and testing datasets using the fit_transform and transform methods. This step prepares the data for further analysis or modeling.

Saving Preprocessing Object: The code saves the preprocessing object to a specified file path using the save_object function. This allows the preprocessing steps to be applied consistently on new data later.

Returning Results: The code returns the transformed training and testing datasets, the file path of the saved preprocessing object, and other relevant information as a tuple.
        '''