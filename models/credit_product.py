from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from models.database import Base

class CreditProduct(Base):
    __tablename__ = 'credit_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type_product = Column(String, nullable=False, index=True)
    percent = Column(Float, nullable=False)
    repayment_period = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    recommended_payment = Column(Float, nullable=False)

    requests = relationship('Request', back_populates='credit_product')
