from jwt import encode
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.users import read_one_user_by_username
import os

SECRET_KEY = os.getenv("SECRET_KEY")
# SECRET_KEY = "CANTTOUCHTHIS"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(db: Session, username: str, password: str):
    user = read_one_user_by_username(db, username)
    if not user:
        return False
    if not password == user.password:
        return False
    return user
