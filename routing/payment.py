from typing import List

from fastapi import APIRouter, Body
from fastapi.params import Depends

from depends import get_payment_service
from schemas.payment import Payment
from service.payment import PaymentService

router = APIRouter(prefix="/payment", tags=["payment"])

@router.post(
    "/",
    response_model=Payment,
    description="Create a payment",
)
async def create_payment(data=Body(),
                         service: PaymentService=Depends(get_payment_service)) -> Payment:
    payment = service.create(data['payment'])
    return payment


@router.put(
    "/{payment_id}",
    response_model=Payment,
    description="Update a payment",
)
async def update_payment(payment_id: int, data=Body(),
                         service: PaymentService=Depends(get_payment_service)) -> Payment:
    payment = service.update(payment_id, data['payment'])
    return payment


@router.delete(
    "/{payment_id}",
    description="Delete a payment",
)
async def delete_payment(payment_id: int,
                         service: PaymentService=Depends(get_payment_service)):
    service.delete(payment_id)
    return {"message": "Payment deleted"}


@router.get(
    "/user/{inn}",
    response_model=List[Payment],
    description="List all payments for user",
)
async def list_user_payments(inn: int,
                             service: PaymentService=Depends(get_payment_service)) -> List[Payment]:
    payments = service.get_by_user_inn(inn)
    return payments


@router.get(
    "/",
    response_model=List[Payment],
    description="List all payments",
)
async def list_all_payments(service: PaymentService=Depends(get_payment_service)) -> List[Payment]:
    payments = service.get_all()
    return payments
