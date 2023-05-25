import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
#from sklearn.model_selection import GridSearchCV

'''
import os and import sys: These are standard Python libraries for operating system-specific functionalities and system-specific parameters and functions, respectively. They allow you to work with files, directories, and system-related operations.

import numpy as np and import pandas as pd: These are popular libraries in the data science ecosystem. numpy provides support for large, multi-dimensional arrays and mathematical operations, while pandas is used for data manipulation and analysis, providing data structures like DataFrames for handling tabular data.

import dill and import pickle: These libraries are used for object serialization in Python. They allow you to save and load Python objects (such as models or data) to/from files, enabling you to store and reuse them later.

from sklearn.metrics import r2_score: This line imports the r2_score function from the metrics module of scikit-learn library. r2_score is a common evaluation metric used for regression models. It measures the proportion of the variance in the dependent variable that is predictable from the independent variables.

from sklearn.model_selection import GridSearchCV: This line imports the GridSearchCV class from the model_selection module of scikit-learn library. GridSearchCV is used for hyperparameter tuning in machine learning models. It exhaustively searches for the best combination of hyperparameters from a predefined grid of parameter values, using cross-validation to evaluate the model performance.
'''
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    '''
    from src.exception import CustomException: This line imports the CustomException class from the exception module located in the src package. This indicates that there is a custom exception defined in the codebase.

def save_object(file_path, obj): This is a function definition named save_object that takes two parameters: file_path (the path to the file where the object will be saved) and obj (the object to be saved).

dir_path = os.path.dirname(file_path): This line extracts the directory path from the given file_path. It uses the os.path.dirname() function from the os module to get the parent directory of the file.

os.makedirs(dir_path, exist_ok=True): This line creates the directory specified by dir_path if it doesn't already exist. It uses the os.makedirs() function from the os module, and exist_ok=True ensures that no exception is raised if the directory already exists.

with open(file_path, "wb") as file_obj:: This line opens the file_path in write binary mode ("wb"). The with statement ensures proper handling of the file object by automatically closing it when done.

pickle.dump(obj, file_obj): This line uses the pickle.dump() function from the pickle module to serialize and save the obj to the file specified by file_obj.

except Exception as e:: This line begins an exception handling block. It catches any exception that occurs within the preceding try block and assigns it to the variable e.

raise CustomException(e, sys): This line raises a custom exception, CustomException, passing the caught exception (e) and the sys module as arguments. This custom exception may contain additional information or handling specific to the codebase.
    '''
    
def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            

            #gs = GridSearchCV(model,para,cv=3)
            #gs.fit(X_train,y_train)

           # model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
    '''
    def evaluate_models(X_train, y_train, X_test, y_test, models, param): This is a function definition named evaluate_models that takes six parameters: X_train (training data features), y_train (training data labels), X_test (test data features), y_test (test data labels), models (a dictionary of models), and param (a dictionary of model parameters).

report = {}: This line initializes an empty dictionary called report that will store the evaluation scores of the models.

for i in range(len(list(models))):: This line starts a loop over the number of models specified in the models dictionary.

model = list(models.values())[i]: This line retrieves the i-th model from the models dictionary.

para = param[list(models.keys())[i]]: This line retrieves the corresponding parameters for the i-th model from the param dictionary.

gs = GridSearchCV(model, param, cv=3): This line creates an instance of GridSearchCV with the given model and parameters. It performs a grid search with 3-fold cross-validation to find the best hyperparameters for the model.

gs.fit(X_train, y_train): This line fits the grid search object gs to the training data (X_train and y_train), searching for the best hyperparameters.

model.set_params(**gs.best_params_): This line sets the best hyperparameters found by the grid search as the parameters of the model.

model.fit(X_train, y_train): This line fits the model with the updated parameters to the training data.

y_train_pred = model.predict(X_train): This line uses the trained model to make predictions on the training data.

y_test_pred = model.predict(X_test): This line uses the trained model to make predictions on the test data.

train_model_score = r2_score(y_train, y_train_pred): This line calculates the R-squared score between the predicted and actual values of the training data.

test_model_score = r2_score(y_test, y_test_pred): This line calculates the R-squared score between the predicted and actual values of the test data.

report[list(models.keys())[i]] = test_model_score: This line adds the test model score to the report dictionary using the model name as the key.

return report: This line returns the report dictionary containing the evaluation scores of the models.

The except block catches any exception that occurs within the preceding try block. If an exception is caught, it raises a custom exception called CustomException. The CustomException is raised with the original exception (e) and the sys module, which provides information about the exception and the current system.
    '''
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    '''
    The load_object function takes a file_path as input, which represents the path to a file containing an object that needs to be loaded.

Inside the function, it attempts to open the file using the open function in binary read mode ("rb").

If the file is successfully opened, it uses the pickle.load function to load the object from the file. pickle.load reads the binary data from the file and reconstructs the original object.

If the object is successfully loaded, it is returned from the function.

If any exception occurs during the file opening or object loading process, the except block is executed. The exception (e) is caught, and a custom exception called CustomException is raised with the original exception and system information (sys).
    '''