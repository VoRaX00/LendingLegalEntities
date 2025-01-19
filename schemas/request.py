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

class RequestGet(BaseModel):
    id: int
    legal_user_inn: int
    legal_user_name: str
    product_id: int
    product_name: str
    amount: int
    administrator: Administrator
    status: str


class RequestCreate(BaseModel):
    id: int
    legal_user_inn: int
    credit_product_id: int
    status: str

class RequestAdd(BaseModel):
    legal_user_inn: int
    credit_product_id: int