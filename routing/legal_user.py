from datetime import datetime, timezone
from typing import Dict, Any

from fastapi import APIRouter, Path, Body

from fastapi.params import Depends
from rest_framework.request import Request
from rest_framework.response import Response

from service import get_legal_user_service
from schemas.legal_user import LegalUser
from service.exceptions.unauthorized import UnAuthorized
from service.legal_user import LegalUserService
from token_manager.token import TokenManager

router = APIRouter(prefix="/legal_user", tags=["legal_user"])

@router.get(
    "/",
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    },
    description="Get legal user by inn"
)
async def legal_user(request: Request,
                     service: LegalUserService=Depends(get_legal_user_service)) -> LegalUser:
    token = TokenManager().get_token(request)
    payload = TokenManager().decode_token(token)

    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise UnAuthorized(message="Token is expired")

    inn = payload.get('inn')
    if not inn:
        raise UnAuthorized(message="Inner key is missing")
    
    user = service.get_by_inn(inn)
    return user


@router.post(
    "/",
    description="Create legal user",
)
async def create_legal_user(data: LegalUser = Body(..., description='Legal user data'),
                            service: LegalUserService=Depends(get_legal_user_service)) -> LegalUser:
    user = service.create(data)
    return user

@router.post(
    "/",
    description="Login",
)
async def login(response: Response, data: int = Body(..., description='user inn'),
                service: LegalUserService=Depends(get_legal_user_service)) -> dict[str, LegalUser | Any]:
    user = service.get_by_inn(data)
    payload = {
        "inn": user.inn
    }
    token = TokenManager.create_token(payload)
    response.set_cookie(key="token_manager", value=token, httponly=True)
    return {
        "user": user,
        "token_manager": token
    }