from typing import List

from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from service import get_payment_service
from schemas.payment import Payment, PaymentUpdate
from service.payment import PaymentService

router = APIRouter(prefix="/payment", tags=["payment"])

@router.post(
    "/",
    description="Create a payment",
)
async def create_payment(data: Payment = Body(..., description="Payment data"),
                         service: PaymentService=Depends(get_payment_service)) -> Payment:
    payment = service.create(data)
    return payment


@router.put(
    "/{payment_id}",
    description="Update a payment",
)
async def update_payment(payment_id: int = Path(..., description="Payment ID"),
                         data: PaymentUpdate = Body(..., description="Payment data"),
                         service: PaymentService=Depends(get_payment_service)) -> Payment:
    payment = service.update(payment_id, data)
    return payment



@router.get(
    "/user/{inn}",
    description="List all payments for user",
)
async def list_user_payments(inn: int = Path(..., description="User INN"),
                             service: PaymentService=Depends(get_payment_service)) -> List[Payment]:
    payments = service.get_by_user_inn(inn)
    return payments


@router.get(
    "/",
    description="List all payments",
)
async def list_all_payments(service: PaymentService=Depends(get_payment_service)) -> List[Payment]:
    payments = service.get_all()
    return payments
