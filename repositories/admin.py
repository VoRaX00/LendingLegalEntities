from typing import Annotated, Type

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from depends import get_db
from models.admin import Admins
from schemas.admin import Administrator


class AdminRepo:
    def __init__(self, db :Annotated[Session, Depends] = Annotated[Session, Depends(get_db)]):
        self.db = db

    def create(self, admin) -> Administrator:
        self.db.add(admin)
        self.db.commit()
        return admin

    def get_by_email(self, email) -> Type[Admins]:
        admin = self.db.query(Admins).filter(Admins.email == email).one_or_none()
        if admin is None:
            raise HTTPException(status_code=404, detail="admin not found")
        return admin

