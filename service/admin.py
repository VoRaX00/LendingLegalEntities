from repositories.admin import AdminRepo
from schemas.admin import Administrator


class AdminService:

    def __init__(self, repository: AdminRepo) -> None:
        self.repository = repository

    def create_admin(self, admin) -> Administrator:
        return self.repository.create(admin)

    def get_by_email(self, email: str) -> Administrator:
        return self.repository.get_by_email(email)