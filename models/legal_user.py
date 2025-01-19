from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base

class LegalUser(Base):
    __tablename__ = 'legal_users'

    inn = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type_activity = Column(String)
    contact_person = Column(String)
    address = Column(String)

    requests = relationship('Request', back_populates='legal_user')

