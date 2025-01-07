from fastapi import Depends

from repositories.admin import AdminRepo
from repositories.credit_product import CreditProductRepo
from repositories.legal_user import LegalUserRepo
from repositories.payment import PaymentRepo
from repositories.request import RequestRepo
from models.database import get_db
from sqlalchemy.orm import Session

def get_admin_repo(db: Session = Depends(get_db)) -> AdminRepo:
    return AdminRepo(db)

def get_credit_product_repo(db: Session = Depends(get_db)) -> CreditProductRepo:
    return CreditProductRepo(db)

def get_legal_user_repo(db: Session = Depends(get_db)) -> LegalUserRepo:
    return LegalUserRepo(db)

def get_payment_repo(db: Session = Depends(get_db)) -> PaymentRepo:
    return PaymentRepo(db)

def get_request_repo(db: Session = Depends(get_db)) -> RequestRepo:
    return RequestRepo(db)
