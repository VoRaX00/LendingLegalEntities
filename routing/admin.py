from django.core.exceptions import BadRequest
from fastapi import APIRouter, Body, Path, HTTPException
from fastapi.params import Depends

from service import get_admin_service
from schemas.admin import Administrator, AdministratorLogin, AdministratorLoginEmail
from service.admin import AdminService
from token_manager.token import TokenManager

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
    admin = admin_service.create(data)
    return admin

@router.post(
    "/login",
    description="Login admin by email",
)
async def login(data: AdministratorLoginEmail = Body(..., description="Email of the admin"),
                admin_service: AdminService = Depends(get_admin_service)) -> AdministratorLogin:
    admin = admin_service.get_by_email(data.email)
    if not admin:
        raise BadRequest("Invalid email")

    payload = {
        "email": data.email,
        "type": "admin"
    }

    token = TokenManager.create_token(payload)
    resp = AdministratorLogin
    resp.token = token
    return resp