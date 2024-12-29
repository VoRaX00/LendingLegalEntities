from repositories.admin import AdminRepo
from schemas.admin import Administrator


class AdminService:

    def __init__(self, repository: AdminRepo) -> None:
        self.repository = repository

    def create_admin(self, admin) -> Administrator:
        result = self.repository.create(admin)
        return result

    def get_by_email(self, email: str) -> Administrator:
        result = self.repository.get_by_email(email)
        return result