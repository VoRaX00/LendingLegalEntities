from typing import List

from repositories.credit_product import CreditProductRepo
from schemas.credit_product import CreditProduct


class CreditProductService:
    def __init__(self, repository: CreditProductRepo):
        self.repository = repository

    def create(self, credit_product) -> CreditProduct:
        return self.repository.create(credit_product)

    def delete(self, id: int):
        self.repository.delete(id)

    def get_all(self) -> List[CreditProduct]:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> CreditProduct:
        return self.repository.get_by_id(id)