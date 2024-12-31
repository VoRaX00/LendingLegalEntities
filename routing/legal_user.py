from fastapi import APIRouter, Path, Body
from fastapi.params import Depends

from depends import get_legal_user_service
from schemas.legal_user import LegalUser
from service.legal_user import LegalUserService

router = APIRouter(prefix="/legal_user", tags=["legal_user"])

@router.get(
    "/{inn}",
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    },
    response_model=LegalUser,
    description="Get legal user by inn"
)
async def legal_user(inn: int = Path(..., description='User INN'),
                     service: LegalUserService=Depends(get_legal_user_service)) -> LegalUser:
    user = service.get_by_inn(inn)
    return user


@router.post(
    "/",
    description="Create legal user",
)
async def create_legal_user(data: LegalUser = Body(..., description='Legal user data'),
                            service :LegalUserService=Depends(get_legal_user_service)) -> LegalUser:
    user = service.create(data)
    return user