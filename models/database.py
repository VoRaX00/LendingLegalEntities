from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

URL_PATH = 'postgresql://postgres:1324@localhost:4928/lending'

engine = create_engine(URL_PATH)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase): pass