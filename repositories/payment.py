from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from depends import get_db
from models.payment import Payment


class PaymentRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, payment: Payment) -> Payment:
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def update(self, payment_id: int, payment: Payment) -> Payment:
        self.db.query(Payment).filter(Payment.id == payment_id).update({
            Payment.date_payment: payment.date_payment,
            Payment.recommended_payment: payment.recommended_payment,
            Payment.delay: payment.delay,
            Payment.date_replenishment: payment.date_replenishment,
        })
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def delete(self, payment_id):
        self.db.query(Payment).filter(Payment.id == payment_id).delete()
        self.db.commit()


    def get_by_user_inn(self, user_inn) -> List[Payment]:
        payments = self.db.query(Payment).filter(Payment.legal_user_inn == user_inn).all()
        return payments

    def get_by_id(self, payment_id) -> Payment | None:
        payment = self.db.query(Payment).filter(Payment.id == payment_id).first()
        return payment

    def get_all(self) -> List[Payment]:
        payments = self.db.query(Payment).all()
        return payments