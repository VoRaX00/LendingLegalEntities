import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

db_password = os.getenv('DB_PASSWORD')
URL_PATH = 'postgresql://postgres:' + db_password + '@localhost:4928/LendingDB'

engine = create_engine(URL_PATH)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase): pass