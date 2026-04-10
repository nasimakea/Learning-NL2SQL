# src/utils/exception.py

import sys


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(str(error_message))
        self.error_message = str(error_message)

    def __str__(self):
        return self.error_message