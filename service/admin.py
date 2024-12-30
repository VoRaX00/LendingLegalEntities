from fastapi import HTTPException
from sqlalchemy.dialects.postgresql.asyncpg.AsyncAdapt_asyncpg_dbapi import InternalServerError

from models.admin import Admins
from repositories.admin import AdminRepo
from schemas.admin import Administrator
from service.exceptions.already_exists import AlreadyExistsException
from service.exceptions.not_found import NotFoundException


def map_schema_to_model(administrator: Administrator) -> Admins:
    return Admins(email=administrator.email, login=administrator.login,)

class AdminService:
    def __init__(self, repository: AdminRepo) -> None:
        self.repository = repository

    def create_admin(self, admin: Administrator) -> Administrator:
        existing_admin = self.repository.get_by_email(admin.email)
        if existing_admin:
            raise AlreadyExistsException('Admin already exists')

        model = map_schema_to_model(admin)
        try:
            created_admin = self.repository.create(model)
        except Exception as e:
            raise InternalServerError()
        return Administrator.model_validate(created_admin)

    def get_by_email(self, email: str) -> Administrator:
        admin = self.repository.get_by_email(email)
        if admin is None:
            raise NotFoundException('Admin not found')
        return Administrator.model_validate(admin)