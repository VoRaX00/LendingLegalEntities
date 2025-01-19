from typing import List

from repositories.payment import PaymentRepo
from schemas.legal_user import LegalUser
from schemas.payment import Payment, PaymentUpdate
from models.payment import Payment as PaymentModels
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


class PaymentService:
    def __init__(self, repository: PaymentRepo):
        self.repository = repository

    def create(self, payment: Payment) -> Payment:
        model = self.map_schemas_to_model(payment)

        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()
        return self.map_model_to_schema(model)

    def update(self, payment_id: int, payment: PaymentUpdate) -> Payment:
        exists_payment = self.repository.get_by_id(payment_id)
        if exists_payment is None:
            raise NotFoundException("Payment not found")

        if payment.recommended_payment != None:
            exists_payment.recommended_payment = payment.recommended_payment
        if payment.delay != None:
            exists_payment.delay = payment.delay
        if payment.date_replenishment != None:
            exists_payment.date_replenishment = payment.date_replenishment

        try:
            model = self.repository.update(payment_id, exists_payment)
        except Exception as e:
            raise InternalServerException()
        return self.map_model_to_schema(model)

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
        result = []
        for payment in payments:
            result.append(self.map_model_to_schema(payment))
        return result

    def get_all(self) -> List[Payment]:
        payments = self.repository.get_all()
        result = []
        for payment in payments:
            result.append(self.map_model_to_schema(payment))
        return result

    @staticmethod
    def map_schemas_to_model(payment: Payment) -> PaymentModels:
        return PaymentModels(
            legal_user_inn=payment.legal_user.inn,
            recommended_payment=payment.recommended_payment,
            delay=payment.delay,
            date_payment=payment.date_payment,
            date_replenishment=payment.date_replenishment,
        )

    @staticmethod
    def map_model_to_schema(payment: PaymentModels) -> Payment:
        return Payment(
            id=payment.id,
            legal_user_inn=payment.legal_user_inn,
            recommended_payment=payment.recommended_payment,
            delay=payment.delay,
            date_payment=payment.date_payment,
            date_replenishment=payment.date_replenishment,
        )