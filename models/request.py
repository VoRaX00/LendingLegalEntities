from sqlalchemy import Column, Integer, ForeignKey, String

from database import Base

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    legal_user_id = Column(Integer, ForeignKey('users.id'))
    credit_product_id = Column(Integer, ForeignKey('credit_product.id'))
    status = Column(String)
    administrator_id = Column(Integer, ForeignKey('users.id'))