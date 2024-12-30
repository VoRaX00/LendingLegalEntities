from typing import List

from repositories.credit_product import CreditProductRepo
from schemas.credit_product import CreditProduct
from models.credit_product import CreditProduct as CreditProductModel
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


def map_schemas_to_model(product: CreditProduct) -> CreditProductModel:
    return CreditProductModel(name=product.name, type_product=product.type_product,
                              percent=product.percent, repayment_period=product.repayment_period,
                              amount=product.amount, recommended_payment=product.recommended_payment,
                              )

class CreditProductService:
    def __init__(self, repository: CreditProductRepo):
        self.repository = repository

    def create(self, credit_product: CreditProduct) -> CreditProduct:
        model = map_schemas_to_model(credit_product)
        try:
            result = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()

        return CreditProduct.model_validate(result)

    def delete(self, product_id: int):
        try:
            self.repository.delete(product_id)
        except Exception as e:
            raise InternalServerException()

    def get_all(self) -> List[CreditProduct]:
        products = self.repository.get_all()
        result = List[CreditProductModel]()

        for product in products:
            result.append(CreditProduct.model_validate(product))
        return result

    def get_by_id(self, product_id: int) -> CreditProduct:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise NotFoundException("Product not found")
        return CreditProduct.model_validate(product)