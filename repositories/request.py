from typing import List
from sqlalchemy.orm import Session
from models.request import Request


class RequestRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request: Request) -> Request:
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request

    def update(self, request_id: int, request: Request) -> Request:
        self.db.query(Request).filter(Request.id == request_id).update({
            Request.status: request.status,
        })
        self.db.commit()
        self.db.refresh(request)
        return request

    def get_by_inn(self, inn) -> List[Request]:
        requests = self.db.query(Request).filter(Request.legal_user_inn == inn).all()
        return requests

    def get_all(self) -> List[Request]:
        requests = self.db.query(Request).all()
        return requests

    def get_by_id(self, request_id) -> Request | None:
        request = self.db.query(Request).filter(Request.id == request_id).one_or_none()
        return request