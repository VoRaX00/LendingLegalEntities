from repositories.legal_user import LegalUserRepo
from schemas.legal_user import LegalUser


class LegalUserService:

    def __init__(self, repository: LegalUserRepo):
        self.repository = repository

    def create(self, user) -> LegalUser:
        return self.repository.create(user)

    def get_by_inn(self, inn: int) -> LegalUser:
        return self.repository.get_by_inn(inn)