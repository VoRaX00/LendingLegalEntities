from pydantic import BaseModel

from schemas.admin import Administrator
from schemas.credit_product import CreditProduct
from schemas.legal_user import LegalUser

class Request(BaseModel):
    status: str
    email: str


class RequestGet(BaseModel):
    id: int
    legal_user_inn: int
    product_id: int
    amount: int
    administrator_email: str
    status: str


class RequestCreate(BaseModel):
    id: int
    legal_user_inn: int
    credit_product_id: int
    status: str

class RequestAdd(BaseModel):
    legal_user_inn: int
    credit_product_id: int