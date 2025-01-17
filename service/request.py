from typing import List

from repositories.request import RequestRepo
from schemas.admin import Administrator
from schemas.request import Request, RequestAdd, RequestCreate, RequestGet
from models.request import Request as RequestModel
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


class RequestService:
    def __init__(self, repository: RequestRepo):
        self.repository = repository

    def create(self, req: RequestAdd) -> RequestCreate:
        model = self.map_schemas_to_model(req)
        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()

        return self.map_model_to_schema(model)

    def update(self, request_id: int, req) -> RequestGet:
        exists_request = self.repository.get_by_id(request_id)
        if exists_request is None:
            raise NotFoundException("Request not found")

        exists_request.administrator_email = req.email
        exists_request.status = req.status

        try:
            model =self.repository.update(request_id, exists_request)
        except Exception as e:
            raise InternalServerException()

        return self.map_model_to_schema_get(model)

    def get_by_inn(self, inn: int) -> List[RequestGet]:
        requests =  self.repository.get_by_inn(inn)
        result = []
        for req in requests:
            result.append(self.map_model_to_schema_get(req))
        return result


    def get_all(self) -> List[RequestGet]:
        requests = self.repository.get_all()
        result = []
        for req in requests:
            result.append(self.map_model_to_schema_get(req))
        return result

    @staticmethod
    def map_schemas_to_model(req: RequestAdd) -> RequestModel:
        return RequestModel(
            legal_user_inn=req.legal_user_inn,
            credit_product_id=req.credit_product_id,
        )

    @staticmethod
    @staticmethod
    def map_model_to_schema_get(req: RequestModel) -> RequestGet:
        email = req.administrator_email or "Не определён"
        return RequestGet(
            id=req.id,
            legal_user_inn=req.legal_user_inn,
            product_id=req.credit_product_id,
            amount=req.credit_product.amount,
            administrator_email=email,
            status=req.status,
        )

    @staticmethod
    def map_model_to_schema(req: RequestModel) -> RequestCreate:
        # user = LegalUser(inn=req.legal_user_inn)
        # product = CreditProduct(id=req.credit_product_id)
        return RequestCreate(
            id=req.id,
            legal_user_inn=req.legal_user_inn,
            credit_product_id=req.credit_product_id,
            status=req.status,
        )