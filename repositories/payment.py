from typing import List

from schemas.payment import Payment


class PaymentRepo:
    def create(self, payment):
        pass

    def update(self, payment):
        pass

    def delete(self, payment_id):
        pass

    def get_by_user_inn(self, user_inn) -> List[Payment]:
        pass

    def get_all(self) -> List[Payment]:
        pass