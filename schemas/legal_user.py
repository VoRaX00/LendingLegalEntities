from pydantic import BaseModel


class LegalUser(BaseModel):
    inn: int
    name: str
    type_activity: str
    contact_person: str
    address: str

class LegalUserLoginInn(BaseModel):
    inn: int

class LegalUserLogin(BaseModel):
    token: str