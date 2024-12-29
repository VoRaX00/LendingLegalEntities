from pydantic import BaseModel

from schemas.admin import Administrator
from schemas.credit_product import CreditProduct
from schemas.legal_user import LegalUser

class Request(BaseModel):
    id: int
    legal_user: LegalUser
    credit_product: CreditProduct
    status: str
    administrator: Administrator