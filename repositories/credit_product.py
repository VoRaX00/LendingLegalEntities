from typing import List

from schemas.credit_product import CreditProduct


class CreditProductRepo:
    def create(self, credit_product) -> CreditProduct:
        pass

    def delete(self, id):
        pass

    def get_all(self) -> List[CreditProduct]:
        pass

    def get_by_id(self, id) -> CreditProduct:
        pass