from typing import List

from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from depends import get_credit_product_service
from schemas.credit_product import CreditProduct
from service.credit_product import CreditProductService

router = APIRouter(prefix="/credit_product", tags=["credit_product"])

@router.post(
    "/",
    responses={400: {"description": "Bad request"}, 500: {"description": "Internal Server Error"}},
    response_model=CreditProduct,
    description="Create a credit product",
)
async def create_credit_product(data: CreditProduct = Body(),
                                service: CreditProductService =Depends(get_credit_product_service)) -> CreditProduct:
    product = service.create(data)
    return product


@router.delete(
    "/{product_id}",
    description="Delete a credit product",
)
async def delete_credit_product(product_id: int = Path(),
                                service: CreditProductService = Depends(get_credit_product_service)):
    service.delete(product_id)
    return {"message": "Credit product deleted"}


@router.get(
    "/",
    responses={500: {"description": "Internal Server Error"}},
    response_model=List[CreditProduct],
    description="Get all credit products",
)
async def get_all_credit_products(service: CreditProductService = Depends(get_credit_product_service)) -> List[CreditProduct]:
    products = service.get_all()
    return products


@router.get(
    "/{product_id}",
    responses={
        404: {"description": "Not found"}, 500: {"description": "Internal Server Error"}
    },
    response_model=CreditProduct,
    description="Get a credit product by id",
)
async def get_credit_product(product_id: int = Path(),
                             service: CreditProductService = Depends(get_credit_product_service)) -> CreditProduct:
    product = service.get_by_id(product_id)
    return product