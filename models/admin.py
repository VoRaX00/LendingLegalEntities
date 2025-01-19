from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.database import Base

class Admins(Base):
    __tablename__ = 'admins'

    email = Column(String, primary_key=True, index=True)
    login = Column(String, nullable=False)

    requests = relationship('Request', back_populates='administrators')
