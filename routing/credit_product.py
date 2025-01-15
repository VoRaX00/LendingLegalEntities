from typing import List

from fastapi import APIRouter, Body, Path
from fastapi.params import Depends

from service import get_credit_product_service
from schemas.credit_product import CreditProduct
from service.credit_product import CreditProductService

router = APIRouter(prefix="/credit_product", tags=["credit_product"])

@router.post(
    "/",
    description="Create a credit product",
)
async def create_credit_product(data: CreditProduct=Body(..., description="Credit product data"),
                                service: CreditProductService=Depends(get_credit_product_service)) -> CreditProduct:
    product = service.create(data)
    return product


@router.get(
    "/",
    description="Get all credit products",
)
async def get_all_credit_products(service: CreditProductService = Depends(get_credit_product_service)) -> List[CreditProduct]:
    products = service.get_all()
    return products


@router.get(
    "/{product_id}",
    description="Get a credit product by id",
)
async def get_credit_product(product_id: int = Path(..., description="Product ID"),
                             service: CreditProductService = Depends(get_credit_product_service)) -> CreditProduct:
    product = service.get_by_id(product_id)
    return product