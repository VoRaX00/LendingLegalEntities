from datetime import datetime
from pydantic import BaseModel
from schemas.legal_user import LegalUser


class Payment(BaseModel):
    id: int
    legal_user: LegalUser
    recommended_payment: float
    delay: int
    date_payment: datetime
    date_replenishment: datetime
