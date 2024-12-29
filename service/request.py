from typing import List

from repositories.request import RequestRepo
from schemas.request import Request


class RequestService:
    def __init__(self, repository: RequestRepo):
        self.repository = repository

    def create(self, request) -> Request:
        return self.repository.create(request)

    def update(self, request_id: int, request) -> Request:
        return self.repository.update(request_id, request)

    def get_by_inn(self, inn: int) -> List[Request]:
        return self.repository.get_by_inn(inn)

    def get_all(self) -> List[Request]:
        return self.repository.get_all()
