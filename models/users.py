from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import Column,String,Date,Integer
from db import Base
from schemas.users import UserInsertion

class Users(Base):
    __tablename__ = 'users'

    userid = Column(Integer, primary_key=True)  # Changed from UUID to Integer
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    createdat = Column(Date, nullable=True, server_default="CURRENT_DATE")

def read_one_user_by_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()

def insert_user(db: Session, user: UserInsertion):
    db_user = read_one_user_by_username(db,user.username)
    
    if not db_user:
        # Create new record
        db_user = Users( **user.__dict__)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {'msg': 'created', 'user': db_user}
    else:
        raise HTTPException(status_code=400, detail="User Already Exists")


def update_user(db: Session, user: UserInsertion):
    db_user = read_one_user_by_username(db,user.username)
    
    if db_user:
        # Update existing record
        db.query(Users).filter(Users.username == user.username).update(user.__dict__)
        db.commit()
        db.refresh(db_user)
        return {'msg': 'created', 'user': db_user}
    else:
        raise HTTPException(status_code=404, detail="User Not Found")


def delete_user(db: Session, userid: str):
    sql = db.query(Users).filter(Users.userid == userid)
    sql.delete()
    db.commit()
    return {'msg': 'Users has been deleted', 'userid': userid}