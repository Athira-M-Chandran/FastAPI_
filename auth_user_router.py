from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from auth_user_connection import Session
from auth_model_users import User

router = APIRouter()

app = FastAPI()

@router.get("/users/")
def get_user():
    with Session() as session:
        users = session.query(User).all()
        if users is None:
            raise HTTPException(status_code = 404, detail = "Users not found")
        return users

    
@router.get("/users/{user_id}")
def get_user_id(user_id : int):
    with Session() as session:
        user = session.query(User).get(user_id)
        if user is None:
            raise HTTPException(status_code = 404, detail = "Users not found")
        return user


app.include_router(router)