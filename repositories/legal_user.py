from schemas.legal_user import LegalUser


class LegalUserRepo:
    def create(self, legal_user) -> LegalUser:
        pass

    def get_by_inn(self, inn: int) -> LegalUser:
        pass