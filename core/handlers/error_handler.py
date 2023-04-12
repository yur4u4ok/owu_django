from core.enums.error_enum import ErrorEnum
from core.exceptions.jwt_exception import JWTException

from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_error_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JWTException': _jwt_validate_error
    }

    response = exception_handler(exc, context)
    exc_name = exc.__class__.__name__

    if exc_name in handlers:
        return handlers[exc_name](exc, context)

    return response


def _jwt_validate_error(exc: JWTException, context: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
