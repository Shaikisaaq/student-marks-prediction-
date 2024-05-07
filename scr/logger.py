# Description: This file contains the logger configuration for the project.

# The logger configuration is done in the logger.py file.

# Importing the required libraries and modules. 
# The os module is used to interact with the operating system.

# The datetime module is used to work with dates and times.

# The logging module is used to log the messages to the console and the file.

import logging
import os
from datetime import datetime

# The LOG_FILE variable is used to store the name of the log file.
LOG_FILE= f"{datetime.now().strftime('%Y-%m-%d')}.log"

# The logs_path variable is used to store the path of the log file.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# os.makedirs() method is used to create a directory named logs in the current working directory.
os.makedirs(logs_path,exist_ok=True)

# os.path.join() method is used to join the path of the logs directory and the log file.
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig() method is used to configure the logging module. filename parameter is used to specify the file to which the logs will be written. level parameter is used to specify the level of the logs. format parameter is used to specify the format of the logs.

logging.basicConfig(filename=LOG_FILE_PATH,level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s'
)
 