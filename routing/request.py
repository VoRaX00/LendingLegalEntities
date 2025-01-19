from typing import List

from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from service import get_request_service
from schemas.request import Request, RequestAdd, RequestCreate, RequestGet
from service.request import RequestService

router = APIRouter(prefix="/request", tags=["request"])


@router.post(
    "/",
    description="Create a new request",
)
async def create_request(data: RequestAdd = Body(..., description="Request data"),
                         service: RequestService=Depends(get_request_service)) -> RequestCreate:
    req = service.create(data)
    return req

@router.put(
    "/{request_id}",
    description="Update a request",
)
async def update_request(request_id: int = Path(..., description="Request id"),
                         data: Request = Body(..., description="Request data"),
                         service: RequestService=Depends(get_request_service)) -> RequestGet:
    req = service.update(request_id, data)
    return req


@router.get(
    "/user/{inn}",
    description="List all requests for user",
)
async def get_user_requests(inn: int = Path(..., description="Request id"),
                      service: RequestService=Depends(get_request_service)) -> List[RequestGet]:
    req = service.get_by_inn(inn)
    return req


@router.get(
    "/",
    description="List all requests",
)
async def get_requests(service: RequestService=Depends(get_request_service)) -> List[RequestGet]:
    reqs = service.get_all()
    return reqs
