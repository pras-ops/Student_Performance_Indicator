import logging
import os
from datetime import datetime

'''
import logging: This line imports the logging module, which is a built-in module in Python used for logging and tracking events or messages during program execution. It allows you to record information, warnings, errors, and other messages to various outputs such as the console, files, or external services.

import os: This line imports the os module, which provides a way to interact with the operating system. It allows you to perform various operations related to file and directory manipulation, environment variables, and more.

from datetime import datetime: This line imports the datetime class from the datetime module. The datetime class provides functions to work with dates and times in Python.
'''

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

'''
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log": This line creates a string variable called LOG_FILE that contains the current date and time formatted as "month_day_year_hour_minute_second.log". It uses the datetime.now().strftime() function to retrieve the current date and time and format it accordingly.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE): This line creates a string variable called logs_path by joining multiple components together using os.path.join(). It combines the current working directory (os.getcwd()), the "logs" directory name, and the LOG_FILE variable. This creates a full file path to the desired log file.

os.makedirs(logs_path,exist_ok=True): This line creates the directory structure necessary for the log file. It uses os.makedirs() function to create directories along the specified path (logs_path). The exist_ok=True parameter ensures that if the directories already exist, no error is raised.
'''
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

'''
LOG_FILE_PATH: This is a variable that will store the complete path to the log file. It is being assigned a value in the code.

os.path.join(): This is a function from the os.path module in Python. It is used to join different parts of a file path into a single path. It takes multiple arguments, which are the parts of the path that need to be joined together.

logs_path: This is a variable that represents the directory path where the log file will be stored. It is one of the parts that will be joined together to create the complete path.

LOG_FILE: This is a variable that represents the name of the log file. It is another part that will be joined with the logs_path to create the complete path.
'''


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

'''
logging.basicConfig(: Starts the configuration of the logging module in Python.

filename=LOG_FILE_PATH: Specifies the path to the log file where the log messages will be written. LOG_FILE_PATH should be replaced with the actual file path as a string.

format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s": Defines the format of the log messages. It specifies how the log messages should be structured and what information should be included. Here's a breakdown of the format placeholders:

%(asctime)s: Represents the timestamp of the log message.
%(lineno)d: Represents the line number in the source code where the log message was generated.
%(name)s: Represents the name of the logger that generated the log message.
%(levelname)s: Represents the log level (e.g., INFO, WARNING, ERROR) of the log message.
%(message)s: Represents the actual log message.
level=logging.INFO: Sets the logging level to INFO. This means that only log messages with a level of INFO or above (e.g., INFO, WARNING, ERROR, CRITICAL) will be recorded in the log file. Lower-level log messages (e.g., DEBUG) will be ignored.
'''