from pydantic.v1 import BaseModel


class CreditProduct(BaseModel):
    id: int
    name: str
    type_product: str
    percent: float
    repayment_period: int
    amount: float
    recommended_payment: float