from sqlalchemy import Column, Integer, ForeignKey, Float, Date

from database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    legal_user_inn = Column(Integer, ForeignKey('legal_users.inn'))
    recommended_payment = Column(Float)
    delay = Column(Integer)
    date_payment = Column(Date)
    date_replenishment = Column(Date, nullable=True)