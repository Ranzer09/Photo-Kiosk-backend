from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "postgresql://postgres:admin@localhost:5432/photo-kiosk")

engine= create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():   
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)
