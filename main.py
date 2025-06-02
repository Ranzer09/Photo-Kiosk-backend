from fastapi import FastAPI
from routers.users import  users
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()

app.include_router(users)
