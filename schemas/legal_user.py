from pydantic import BaseModel


class LegalUser(BaseModel):
    inn: int
    name: str
    type_activity: str
    contact_person: str
    address: str