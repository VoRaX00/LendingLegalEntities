from service.admin import AdminService
from service.credit_product import CreditProductService
from service.legal_user import LegalUserService
from service.payment import PaymentService
from service.request import RequestService
from repositories import (
    get_admin_repo,
    get_credit_product_repo,
    get_legal_user_repo,
    get_payment_repo,
    get_request_repo, AdminRepo, CreditProductRepo, LegalUserRepo, PaymentRepo, RequestRepo,
)
from fastapi.params import Depends

def get_admin_service(repo: AdminRepo = Depends(get_admin_repo)) -> AdminService:
    return AdminService(repo)

def get_credit_product_service(repo: CreditProductRepo = Depends(get_credit_product_repo)) -> CreditProductService:
    return CreditProductService(repo)

def get_legal_user_service(repo: LegalUserRepo = Depends(get_legal_user_repo)) -> LegalUserService:
    return LegalUserService(repo)

def get_payment_service(repo: PaymentRepo = Depends(get_payment_repo)) -> PaymentService:
    return PaymentService(repo)

def get_request_service(repo: RequestRepo = Depends(get_request_repo)) -> RequestService:
    return RequestService(repo)
