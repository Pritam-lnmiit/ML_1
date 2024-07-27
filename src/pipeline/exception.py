import sys



def error_message_details(error,error_details:sys):
    _,_,ecc_tb=error_details.exc_info()
    file_name=ecc_tb.tb_frame.f_code.co_filename
    error_message='Error cooured in python script name[{0}] line number[{1}]'.format()
    file_name,ecc_tb.tb_lineno,str(error)

    return error_message


class CustomException(Exception):
    def __init__(self,error_mesaage,error_detail:sys):
        super.__init__(error_mesaage)
        self.error_message=error_message_details(error_mesaage,error_details=error_detail)

    def __str__(self):
        return self.error_message