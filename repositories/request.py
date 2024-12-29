from typing import List

from schemas.request import Request


class RequestRepo:
    def create(self, request) -> Request:
        pass

    def update(self, request_id: int, request) -> Request:
        pass

    def get_by_inn(self, inn) -> List[Request]:
        pass

    def get_all(self) -> List[Request]:
        pass