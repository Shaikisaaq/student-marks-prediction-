import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error: {} in file: {} at line: {}".format(error,file_name,exc_tb.tb_lineno)
    return error_message

# when ever you raise any execption use this class to raise the exception with the error message and the error detail.

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error
    
    
