from typing import List

from urllib3 import request

from repositories.request import RequestRepo
from routing.legal_user import legal_user
from schemas.admin import Administrator
from schemas.credit_product import CreditProduct
from schemas.legal_user import LegalUser
from schemas.request import Request
from models.request import Request as RequestModel
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


class RequestService:
    def __init__(self, repository: RequestRepo):
        self.repository = repository

    def create(self, req: Request) -> Request:
        model = self.map_schemas_to_model(req)
        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()

        return self.map_model_to_schema(model)

    def update(self, request_id: int, req) -> Request:
        exists_request = self.repository.get_by_id(request_id)
        if exists_request is None:
            raise NotFoundException("Request not found")

        model = self.map_schemas_to_model(req)
        try:
            model =self.repository.update(request_id, model)
        except Exception as e:
            raise InternalServerException()

        return self.map_model_to_schema(model)

    def get_by_inn(self, inn: int) -> List[Request]:
        requests =  self.repository.get_by_inn(inn)
        result = List[Request]()
        for req in requests:
            result.append(self.map_model_to_schema(req))
        return result


    def get_all(self) -> List[Request]:
        requests = self.repository.get_all()
        result = List[Request]()
        for req in requests:
            result.append(self.map_model_to_schema(req))
        return result

    @staticmethod
    def map_schemas_to_model(req: Request) -> RequestModel:
        return RequestModel(
            id=req.id,
            legal_user_inn=req.legal_user.inn,
            credit_product_id=req.credit_product.id,
            status=req.status,
            administrator_email=req.administrator.email,
        )

    @staticmethod
    def map_model_to_schema(req: RequestModel) -> Request:
        return Request(
            id=req.id,
            legal_user=LegalUser(inn=req.legal_user_inn),
            credit_product=CreditProduct(id=req.credit_product_id),
            status=req.status,
            administrator=Administrator(email=req.administrator_email)
        )