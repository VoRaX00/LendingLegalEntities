from repositories.admin import AdminRepo
from service.admin import AdminService

admin_repository = AdminRepo()
admin_service = AdminService(admin_repository)

def get_admin_service():
    return admin_service