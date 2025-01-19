from datetime import datetime, timezone
from typing import Dict, Any

from django.core.exceptions import BadRequest
from fastapi import APIRouter, Path, Body, Request, Response

from fastapi.params import Depends

from service import get_legal_user_service
from schemas.legal_user import LegalUser, LegalUserLogin, LegalUserLoginInn
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
    "/login",
    description="Login",
)
async def login(data: LegalUserLoginInn = Body(..., description='user inn'),
                service: LegalUserService=Depends(get_legal_user_service)) -> LegalUserLogin:
    user = service.get_by_inn(data.inn)
    if user is None:
        raise BadRequest("Неверный инн")

    payload = {
        "inn": user.inn,
        "type": "user"
    }
    token = TokenManager.create_token(payload)
    resp = LegalUserLogin
    resp.token = token
    return resp