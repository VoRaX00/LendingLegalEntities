from fastapi import APIRouter, Body, Path, HTTPException
from fastapi.params import Depends

from depends import get_admin_service
from schemas.admin import Administrator
from service.admin import AdminService

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get(
    "/",
    description="Get admin by email",
)
async def get_by_email(email: str = Path(..., description="Email of the admin"),
                       admin_service: AdminService = Depends(get_admin_service)) -> Administrator:
    try:
        admin = admin_service.get_by_email(email)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    return admin

@router.post(
    "/",
    description="Create admin by email",
)
async def create_admin(data: Administrator = Body(..., description="Administrator data"),
                       admin_service: AdminService = Depends(get_admin_service)) -> Administrator:
    admin = admin_service.create_admin(data)
    return admin