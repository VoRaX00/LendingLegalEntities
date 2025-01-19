from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from models.database import Base

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    legal_user_inn = Column(Integer, ForeignKey('legal_users.inn'))
    credit_product_id = Column(Integer, ForeignKey('credit_products.id'))
    status = Column(String, default='в обработке')
    administrator_email = Column(String, ForeignKey('admins.email'), nullable=True)

    legal_user = relationship('LegalUser', back_populates='requests')
    credit_product = relationship('CreditProduct', back_populates='requests')
    administrators = relationship('Admins', back_populates='requests')