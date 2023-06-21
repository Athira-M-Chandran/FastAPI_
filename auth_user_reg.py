from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from auth_model_users import User
from auth_user_connection import Session
import urllib

app = FastAPI()

class UserRegistrationRequest(BaseModel):
    username : str
    password : str
    email : str

@app.post("/register/")
def register_users(user_data_list: List[UserRegistrationRequest]):
    with Session() as session:
        for user_data in user_data_list:
            username = user_data.username
            password = user_data.password
            email = user_data.email

            user = User(username=username, email=email)
            user.set_password(password)

            session.add(user)
            
        session.commit()