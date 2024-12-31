from typing import List

from repositories.request import RequestRepo
from schemas.request import Request
from models.request import Request as RequestModel
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


def map_schemas_to_model(request: Request) -> RequestModel:
    return RequestModel(
        id=request.id,
        legal_user_inn=request.legal_user.inn,
        credit_product_id=request.credit_product.id,
        status=request.status,
        administrator_email=request.administrator.email,
    )

class RequestService:
    def __init__(self, repository: RequestRepo):
        self.repository = repository

    def create(self, request: Request) -> Request:
        model = map_schemas_to_model(request)
        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()

        return Request.model_validate(model)

    def update(self, request_id: int, request) -> Request:
        exists_request = self.repository.get_by_id(request_id)
        if exists_request is None:
            raise NotFoundException("Request not found")

        model = map_schemas_to_model(request)
        try:
            model =self.repository.update(request_id, model)
        except Exception as e:
            raise InternalServerException()

        return Request.model_validate(model)

    def get_by_inn(self, inn: int) -> List[Request]:
        requests =  self.repository.get_by_inn(inn)
        result = List[Request]()
        for request in requests:
            result.append(Request.model_validate(request))
        return result


    def get_all(self) -> List[Request]:
        requests = self.repository.get_all()
        result = List[Request]()
        for request in requests:
            result.append(Request.model_validate(request))
        return result
