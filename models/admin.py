from sqlalchemy import Column, String
from models.database import Base

class Admins(Base):
    __tablename__ = 'admins'

    email = Column(String, primary_key=True, index=True)
    login = Column(String, nullable=False)

