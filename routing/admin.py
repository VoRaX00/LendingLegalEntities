from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from depends import get_admin_service
from schemas.admin import Administrator
from service.admin import AdminService

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get(
    "/",
    responses={
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    },
    response_model=Administrator,
    description="Get admin by email",
)
async def get_by_email(email: str = Path(), admin_service: AdminService = Depends(get_admin_service)) -> Administrator:
    admin = admin_service.get_by_email(email)
    return admin

@router.post(
    "/",
    responses={
        400: {"description": "Bad request"},
        500: {"description": "Internal Server Error"}
    },
    response_model=Administrator,
    description="Create admin by email",
)
async def create_admin(data = Body(), admin_service: AdminService = Depends(get_admin_service)) -> Administrator:
    admin = admin_service.get_by_email(data["admin"])
    return admin