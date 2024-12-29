from typing import List

from schemas.request import Request


class RequestRepo:
    def create(self, request):
        pass

    def update(self, request):
        pass

    def get_by_inn(self, inn) -> List[Request]:
        pass

    def get_all(self) -> List[Request]:
        pass