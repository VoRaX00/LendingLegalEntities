from typing import Any

from pydantic import BaseModel


class Administrator(BaseModel):
    email: str
    login: str

    model_config = {
        "from_attributes": True
    }

class AdministratorLoginEmail(BaseModel):
    email: str

class AdministratorLogin(BaseModel):
    def __init__(self, /, **data: Any):
        super().__init__(**data)
    token: str