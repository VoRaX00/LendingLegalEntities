from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from schemas.legal_user import LegalUser


class Payment(BaseModel):
    id: int
    legal_user_inn: int
    recommended_payment: float
    delay: int
    date_payment: datetime
    date_replenishment: Optional[datetime]

class PaymentUpdate(BaseModel):
    date_replenishment: Optional[datetime]
    recommended_payment: Optional[float]
    delay: Optional[float]