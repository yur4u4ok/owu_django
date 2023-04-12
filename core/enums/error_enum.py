from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = (
        {'details': 'Token expired or invalid'},
        status.HTTP_400_BAD_REQUEST
    )

    def __init__(self, msg: dict, code):
        self.msg = msg
        self.code = code
