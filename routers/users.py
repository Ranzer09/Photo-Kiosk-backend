
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from models import users as model
from schemas.users import UserInsertion,Login,TokenResponse
from db import get_db
from auth import authenticate_user, create_access_token
from datetime import timedelta

users = APIRouter(
    prefix='/users',
)

@users.get('/{userid}')
async def get_user(
        userid: str,
        db: Session = Depends(get_db),
        response: Response = None
    ):
    user = model.read_one_user(db, userid)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    return user if user else {}

@users.post('/login', response_model=TokenResponse)
async def login(user: Login, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user.username, user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": authenticated_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 

@users.post('')
async def post_users(
        users: UserInsertion,
        db: Session = Depends(get_db)
    ):
    return model.insert_user(db, users)

@users.post('/{userid}')
async def update_users(
        users: UserInsertion,
        db: Session = Depends(get_db)
    ):
    return model.update_user(db, users)

@users.delete('/{userid}')
async def delete_user(
        userid: str,
        db: Session = Depends(get_db)
    ):
    return model.delete_user(db, userid)


