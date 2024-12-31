from sqlalchemy import Column, Integer, String

from models.database import Base

class LegalUser(Base):
    __tablename__ = 'legal_users'

    inn = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type_activity = Column(String)
    contact_person = Column(String)
    address = Column(String)
