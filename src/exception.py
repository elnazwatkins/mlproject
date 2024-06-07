import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    message = str(error)
    error_message = "Error occured in python script name [{0}] line number[{1}] error message [{2}]".format(
        file_name, line_number, message)

    return error_message



class CustomException(Exception):    # CustomException is a child class of Exception class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # inherits error_message from Exception and changes it in the next line
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    