from sqlalchemy import Column, Integer, ForeignKey, String

from models.database import Base

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    legal_user_inn = Column(Integer, ForeignKey('legal_users.inn'))
    credit_product_id = Column(Integer, ForeignKey('credit_products.id'))
    status = Column(String)
    administrator_email = Column(String, ForeignKey('admins.email'))