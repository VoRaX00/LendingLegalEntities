from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session, joinedload

from models.payment import Payment
from models.request import Request


class RequestRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request: Request) -> Request:
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request

    def update(self, request_id: int, request: Request) -> Request:
        self.db.query(Request).filter(Request.id == request_id).update({
            Request.status: request.status,
        })
        self.db.commit()
        self.db.refresh(request)

        if request.status == 'принята':
            # Получаем информацию о кредитном продукте
            credit_product = request.credit_product
            repayment_period = credit_product.repayment_period
            recommended_payment = credit_product.recommended_payment
            start_date = datetime.now().date()  # Текущая дата

            # Генерируем платежи для каждого месяца
            for i in range(repayment_period):
                payment_date = start_date + timedelta(days=30 * (i + 1))
                payment = Payment(
                    legal_user_inn=request.legal_user_inn,
                    recommended_payment=recommended_payment,
                    delay=0,
                    date_payment=payment_date,
                    date_replenishment=None
                )
                self.db.add(payment)

            self.db.commit()

        return request

    def get_by_inn(self, inn) -> List[Request]:
        requests = self.db.query(Request).options(
            joinedload(Request.legal_user),
            joinedload(Request.credit_product),
            joinedload(Request.administrators)
        ).filter(Request.legal_user_inn == inn).all()
        return requests

    def get_all(self) -> List[Request]:
        requests = self.db.query(Request).options(
            joinedload(Request.legal_user),
            joinedload(Request.credit_product),
            joinedload(Request.administrators)
        ).all()
        return requests

    def get_by_id(self, request_id) -> Request | None:
        request = self.db.query(Request).filter(Request.id == request_id).one_or_none()
        return request