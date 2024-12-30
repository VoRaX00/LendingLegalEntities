from typing import cast

from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

class InternalServerException(Exception):
    def __init__(self, message: str = 'Internal Server Error'):
        self.message = message
        super().__init__(self.message)

def internal_server(_: Request, exception: Exception) -> JSONResponse:
    exp = cast(InternalServerException, exception)
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"message": exp.message},
    )
