from models.admin import Admins
from repositories.admin import AdminRepo
from schemas.admin import Administrator
from service.exceptions.already_exists import AlreadyExistsException
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException


class AdminService:
    def __init__(self, repository: AdminRepo) -> None:
        self.repository = repository

    def create(self, admin: Administrator) -> Administrator:
        existing_admin = self.repository.get_by_email(admin.email)
        if existing_admin:
            raise AlreadyExistsException('Admin already exists')

        model = self.map_schema_to_model(admin)
        try:
            created_admin = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()
        return self.map_model_to_schema(created_admin)

    def get_by_email(self, email: str) -> Administrator:
        admin = self.repository.get_by_email(email)
        if admin is None:
            raise NotFoundException('Admin not found')
        return self.map_model_to_schema(admin)

    @staticmethod
    def map_schema_to_model(administrator: Administrator) -> Admins:
        return Admins(email=administrator.email, login=administrator.login)

    @staticmethod
    def map_model_to_schema(admin: Admins) -> Administrator:
        return Administrator(email=admin.email, login=admin.login)