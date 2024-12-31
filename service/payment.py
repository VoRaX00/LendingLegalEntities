from typing import List

from repositories.payment import PaymentRepo
from schemas.payment import Payment
from models.payment import Payment as PaymentModels
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


def map_schemas_to_model(payment: Payment) -> PaymentModels:
    return PaymentModels(
        legal_user_inn=payment.legal_user.inn,
        recommended_payment=payment.recommended_payment,
        delay=payment.delay,
        date_payment=payment.date_payment,
        date_replenishment=payment.date_replenishment,
    )


class PaymentService:
    def __init__(self, repository: PaymentRepo):
        self.repository = repository

    def create(self, payment: Payment) -> Payment:
        model = map_schemas_to_model(payment)

        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()
        return Payment.model_validate(model)

    def update(self, payment_id: int, payment: Payment) -> Payment:
        exists_payment = self.repository.get_by_id(payment_id)
        if exists_payment is None:
            raise NotFoundException("Payment not found")

        model = map_schemas_to_model(payment)

        try:
            model = self.repository.update(payment_id, model)
        except Exception as e:
            raise InternalServerException()
        return Payment.model_validate(model)

    def delete(self, payment_id: int):
        exists_payment = self.repository.get_by_id(payment_id)
        if exists_payment is None:
            raise NotFoundException("Payment not found")

        try:
            self.repository.delete(payment_id)
        except Exception as e:
            raise InternalServerException()

    def get_by_user_inn(self, inn: int) -> List[Payment]:
        payments = self.repository.get_by_user_inn(inn)
        result = List[Payment]()
        for payment in payments:
            result.append(Payment.model_validate(payment))

        return result

    def get_all(self) -> List[Payment]:
        payments = self.repository.get_all()
        result = List[Payment]()
        for payment in payments:
            result.append(Payment.model_validate(payment))
        return result
