from typing import cast

from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

class UnAuthorized(Exception):
    def __init__(self, message: str = 'Internal Server Error'):
        self.message = message
        super().__init__(self.message)

def un_authorized(_: Request, exception: Exception) -> JSONResponse:
    exp = cast(UnAuthorized, exception)
    return JSONResponse(
        status_code=HTTPStatus.UNAUTHORIZED,
        content={"message": exp.message},
    )
