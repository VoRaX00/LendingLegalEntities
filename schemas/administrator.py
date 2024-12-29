from pydantic import BaseModel


class Administrator(BaseModel):
    email: str
    login: str