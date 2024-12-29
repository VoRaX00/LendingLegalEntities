from sqlalchemy import Column, Integer, String
from database import Base

class Admins(Base):
    __tablename__ = 'admins'

    email = Column(String, primary_key=True, index=True)
    login = Column(String, nullable=False)

