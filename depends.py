from repositories.admin import AdminRepo
from repositories.credit_product import CreditProductRepo
from service.admin import AdminService
from service.credit_product import CreditProductService

admin_repository = AdminRepo()
admin_service = AdminService(admin_repository)

def get_admin_service():
    return admin_service

credit_product_repository = CreditProductRepo()
credit_product_service = CreditProductService(credit_product_repository)

def get_credit_product_service():
    return credit_product_service