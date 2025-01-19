from typing import List

from repositories.credit_product import CreditProductRepo
from schemas.credit_product import CreditProduct, CreditProductAdd
from models.credit_product import CreditProduct as CreditProductModel
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


class CreditProductService:
    def __init__(self, repository: CreditProductRepo):
        self.repository = repository

    def create(self, credit_product: CreditProductAdd) -> CreditProduct:
        model = self.map_schemas_to_model(credit_product)
        try:
            result = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()

        return self.map_model_to_schema(result)

    def delete(self, product_id: int):
        try:
            self.repository.delete(product_id)
        except Exception as e:
            raise InternalServerException()

    def get_all(self) -> List[CreditProduct]:
        products = self.repository.get_all()
        result = []

        for product in products:
            result.append(self.map_model_to_schema(product))

        return result

    def get_by_id(self, product_id: int) -> CreditProduct:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise NotFoundException("Product not found")
        return self.map_model_to_schema(product)

    @staticmethod
    def map_schemas_to_model(product: CreditProduct) -> CreditProductModel:
        return CreditProductModel(name=product.name, type_product=product.type_product,
                                  percent=product.percent, repayment_period=product.repayment_period,
                                  amount=product.amount, recommended_payment=product.recommended_payment)

    @staticmethod
    def map_model_to_schema(model: CreditProductModel) -> CreditProduct:
        return CreditProduct(id=model.id, name=model.name, type_product=model.type_product,
                             percent=model.percent, repayment_period=model.repayment_period,
                             amount=model.amount, recommended_payment=model.recommended_payment)