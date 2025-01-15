from typing import Dict, Any

from fastapi import APIRouter, Path, Body
from fastapi.params import Depends

from service import get_legal_user_service
from schemas.legal_user import LegalUser
from service.legal_user import LegalUserService

router = APIRouter(prefix="/legal_user", tags=["legal_user"])

@router.get(
    "/",
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    },
    description="Get legal user by inn"
)
async def legal_user(inn: int = Path(..., description='User INN'),
                     service: LegalUserService=Depends(get_legal_user_service)) -> dict[str, LegalUser | Any]:
    user = service.get_by_inn(inn)

    payload = {
        "inn": user.inn
    }
    token = service.create_access_token(payload)
    return {
        "user": user,
        "token": token
    }


@router.post(
    "/",
    description="Create legal user",
)
async def create_legal_user(data: LegalUser = Body(..., description='Legal user data'),
                            service: LegalUserService=Depends(get_legal_user_service)) -> LegalUser:
    user = service.create(data)
    return user