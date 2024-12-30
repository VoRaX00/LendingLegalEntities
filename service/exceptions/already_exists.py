from typing import cast

from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

class AlreadyExistsException(Exception):
    def __init__(self, message: str = 'Already Exists') -> None:
        self.message = message
        super().__init__(self.message)

def already_exists(_: Request, exception: Exception) -> JSONResponse:
    exp = cast(AlreadyExistsException, exception)
    return JSONResponse(
        status_code=HTTPStatus.CONFLICT,
        content={"message": exp.message},
    )
