from pydantic import BaseModel
from datetime import date
from typing import Optional,TypeVar

T=TypeVar('T')

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