from fastapi import APIRouter
from fastapi.params import Depends

from depends import get_admin_service
from schemas.admin import Administrator
from service.admin import AdminService

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get(
    "/",
    responses={404: {"description": "Not found"}},
    response_model=Administrator,
    description="Получение данных администратора",
)
async def get_by_email(email: str, admin_service: AdminService = Depends(get_admin_service)) -> Administrator:
    admin = admin_service.get_by_email(email)
    return admin