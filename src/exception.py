import sys
from src.logger import logging

'''
import sys: This line imports the sys module in Python. The sys module provides access to various system-specific parameters and functions. 
It allows interaction with the Python interpreter and provides functionalities related to the execution environment.

from src.logger import logging: This line imports the logging object from the logger module located within the src package or directory. 
It assumes that there is a file named logger.py inside the src package or directory, and the logging object is defined within that file. Once imported, the logging object can be used to perform logging operations in the code.
'''



def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

'''
_,_,exc_tb=error_detail.exc_info(): This line retrieves the traceback information associated with the error_detail object. The exc_info() method is called to extract the exception type, exception value, and traceback information. 
The _ is used to ignore the exception type and value, and exc_tb is assigned the traceback object.

file_name=exc_tb.tb_frame.f_code.co_filename: This line retrieves the filename of the Python script where the error occurred. 
It accesses the tb_frame attribute of the traceback object, which represents the current frame of the traceback, and then accesses the f_code attribute to get the code object, from which the filename is obtained.

error_message="Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)): 
This line creates an error message string using string formatting. It includes the filename, line number where the error occurred, and the error message itself. The {0}, {1}, and {2} are placeholders that will be replaced by the corresponding values provided in the format() method.

return error_message: The error message string is returned as the result of the function.
'''

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
'''
class CustomException(Exception)::

The code starts by defining a new class called CustomException.
This class is derived from the built-in Exception class, which is the base class for all exceptions in Python.
By inheriting from Exception, the CustomException class becomes a specialized type of exception that can be raised and handled in code.
def __init__(self, error_message, error_detail: sys)::

This is the constructor method of the CustomException class. It is called when a new instance of the class is created.
The constructor takes two parameters: error_message and error_detail.
error_message represents the main error message that describes the exception.
error_detail represents additional information or details about the exception.
Inside the constructor, the super().__init__(error_message) line calls the constructor of the base Exception class, passing the error_message as an argument.
After that, the code assigns the value of error_detail to self.error_message_detail, which appears to be a separate function that combines the error message and error detail.
def __str__(self)::

This is a special method in Python classes that defines how the object should be represented as a string.
In this case, the __str__ method is overridden to return the error_message.
When an instance of CustomException is converted to a string, the __str__ method is called, and it returns the error message stored in self.error_message.
'''