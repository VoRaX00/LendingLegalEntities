from typing import List
from sqlalchemy.orm import Session
from models.credit_product import CreditProduct


class CreditProductRepo:

    def __init__(self, db: Session):
        self.db = db

    def create(self, credit_product: CreditProduct) -> CreditProduct:
        self.db.add(credit_product)
        self.db.commit()
        self.db.refresh(credit_product)
        return credit_product

    def delete(self, product_id: int):
        self.db.query(CreditProduct).filter(CreditProduct.id == product_id).delete()
        self.db.commit()

    def get_all(self) -> List[CreditProduct]:
        products = self.db.query(CreditProduct).all()
        return products


    def get_by_id(self, product_id: int) -> CreditProduct | None:
        product = self.db.query(CreditProduct).filter(CreditProduct.id == product_id).first()
        return product