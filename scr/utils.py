import os,sys
import pandas as pd 
import numpy as np 
from scr.exeption import CustomException

import dill

def save_object(file_path,object):
    '''
    This function is responsible for saving the object to the file path
    '''
    try:
        dir_path= os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as f:
            dill.dump(object,f)

    except Exception as e:
        raise CustomException(e,sys)