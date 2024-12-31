from fastapi.params import Depends
from sqlalchemy.orm import Session

from models.admin import Admins
from models.database import get_db


class AdminRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, admin: Admins) -> Admins:
        self.db.add(admin)
        self.db.commit()
        return admin

    def get_by_email(self, email: str) -> Admins | None:
        admin: Admins | None = self.db.query(Admins).filter(Admins.email == email).one_or_none()
        return admin

