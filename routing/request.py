from typing import List

from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from depends import get_request_service
from schemas.request import Request
from service.request import RequestService

router = APIRouter(prefix="/request", tags=["request"])


@router.post(
    "/",
    response_model=Request,
    description="Create a new request",
)
async def create_request(data=Body(),
                         service: RequestService=Depends(get_request_service)) -> Request:
    req = service.create(data["request"])
    return req

@router.put(
    "/{request_id}",
    response_model=Request,
    description="Update a request",
)
async def update_request(request_id: int = Path(), data=Body(),
                         service: RequestService=Depends(get_request_service)) -> Request:
    req = service.update(request_id, data["req"])
    return req


@router.get(
    "/user/{inn}",
    response_model=List[Request],
    description="List all requests for user",
)
async def get_request(inn: int = Path(),
                      service: RequestService=Depends(get_request_service)) -> List[Request]:
    req = service.get_by_inn(inn)
    return req


@router.get(
    "/",
    response_model=List[Request],
    description="List all requests",
)
async def get_requests(service: RequestService=Depends(get_request_service)) -> List[Request]:
    reqs = service.get_all()
    return reqs