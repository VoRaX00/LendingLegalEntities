from typing import cast

from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

class NotFoundException(Exception):
    def __init__(self, message: str = "Not Found"):
        self.message = message
        super().__init__(self.message)


def not_found(_: Request, exception: Exception) -> JSONResponse:
    exp = cast(NotFoundException, exception)
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": exp.message},
    )
