from fastapi.params import Depends
from sqlalchemy.orm import Session

from depends import get_db
from models.legal_user import LegalUser


class LegalUserRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, legal_user: LegalUser) -> LegalUser:
        self.db.add(legal_user)
        self.db.commit()
        return legal_user

    def get_by_inn(self, inn: int) -> LegalUser | None:
        user = self.db.query(LegalUser).filter(LegalUser.inn == inn).one_or_none()
        return user