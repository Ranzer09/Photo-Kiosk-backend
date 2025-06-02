from pydantic import BaseModel
from datetime import date
from typing import Optional,TypeVar

T=TypeVar('T')

class UserBase(BaseModel):
    userid: int  # Changed from str to int
    username: str
    password: str
    role: str
    createdat: date

class UserInsertion(BaseModel):
    username: str
    password: str
    role: str

class Login(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    code:str
    status:str
    message:str
    result:Optional[T]=None

class TokenResponse(BaseModel):
    access_token:str
    token_type:str
