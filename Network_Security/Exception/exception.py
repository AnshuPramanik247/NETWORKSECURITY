import sys
from Network_Security.logging.logger import logging

def error_message_detail(error, error_details: sys) -> str:
    _, _, exc_tb = error_details.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details=error_details)

    def __str__(self) -> str:
        return self.error_message


if __name__ == '__main__':
    try:
        logging.info("Testing NetworkSecurityException...")
        raise ValueError("This is a deliberate test error for custom exception verification")
    except Exception as e:
        logging.info(e)
        raise NetworkSecurityException(e, sys)
