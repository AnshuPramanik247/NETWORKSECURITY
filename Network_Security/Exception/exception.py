import os
import sys

# Ensure project root is in sys.path so imports work when running this file directly
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Network_Security.logging.logger import logging


def error_message_detail(error, error_detail=sys, error_details=None) -> str:
    """
    Extracts the script name, line number, and error message from the exception traceback.
    Falls back gracefully if invoked outside an active try...except block.
    """
    details = error_details if error_details is not None else error_detail
    _, _, exc_tb = details.exc_info()

    # If exc_info() had no active traceback, check if the error object itself has one
    if exc_tb is None and hasattr(error, "__traceback__") and error.__traceback__ is not None:
        exc_tb = error.__traceback__

    # Walk to the deepest traceback frame to pinpoint the exact failure line
    while exc_tb and exc_tb.tb_next is not None:
        exc_tb = exc_tb.tb_next

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        # Fallback to the caller's frame when raised directly outside an except block
        try:
            caller_frame = sys._getframe(2)
            file_name = caller_frame.f_code.co_filename
            line_number = caller_frame.f_lineno
        except Exception:
            file_name = "Unknown"
            line_number = "Unknown"

    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] error message [{str(error)}]"
    )
    return error_message


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail=sys, error_details=None):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail, error_details=error_details
        )
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.error_message!r})"


if __name__ == '__main__':
    try:
        logging.info("Testing NetworkSecurityException...")
        # Deliberately raise ZeroDivisionError to verify traceback capture without linter complaints
        raise ZeroDivisionError("division by zero")
    except Exception as e:
        custom_exc = NetworkSecurityException(e, sys)
        logging.info(str(custom_exc))
        print(f"\n[Custom Exception Caught]: {custom_exc}\n")
