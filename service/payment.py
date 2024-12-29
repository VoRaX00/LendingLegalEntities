from typing import List

from repositories.payment import PaymentRepo
from schemas.payment import Payment


class PaymentService:
    def __init__(self, repository: PaymentRepo):
        self.repository = repository

    def create(self, payment) -> Payment:
        return self.repository.create(payment)

    def update(self, payment_id: int, payment) -> Payment:
        return self.repository.update(payment_id, payment)

    def delete(self, payment_id: int):
        self.repository.delete(payment_id)

    def get_by_user_inn(self, inn: int) -> List[Payment]:
        return self.repository.get_by_user_inn(inn)

    def get_all(self) -> List[Payment]:
        return self.repository.get_all()