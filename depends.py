from repositories.admin import AdminRepo
from repositories.credit_product import CreditProductRepo
from repositories.legal_user import LegalUserRepo
from repositories.payment import PaymentRepo
from repositories.request import RequestRepo
from service.admin import AdminService
from service.credit_product import CreditProductService
from service.legal_user import LegalUserService
from service.payment import PaymentService
from service.request import RequestService

admin_repository = AdminRepo()
admin_service = AdminService(admin_repository)
def get_admin_service():
    return admin_service

credit_product_repository = CreditProductRepo()
credit_product_service = CreditProductService(credit_product_repository)
def get_credit_product_service():
    return credit_product_service

legal_user_repository = LegalUserRepo()
legal_user_service = LegalUserService(legal_user_repository)
def get_legal_user_service():
    return legal_user_service

payment_repository = PaymentRepo()
payment_service = PaymentService(payment_repository)
def get_payment_service():
    return payment_service

request_repository = RequestRepo()
request_service = RequestService(request_repository)
def get_request_service():
    return request_service

