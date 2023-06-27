from fastapi import FastAPI, HTTPException, APIRouter
from auth_user_connection import Session
from auth_model_users import User

app = FastAPI()
auth_router = APIRouter(tags=["Authentication"])
user_router = APIRouter(tags=["Users"])

@auth_router.post("/")
def login():
    pass

@user_router.get("/")
def get_users():
    with Session() as session:
        users = session.query(User).all()
        if not users:
            raise HTTPException(status_code=404 , detail= "User not found")
        else:
            return users


@user_router.get("/{user_id}")
def getUser(user_id : int):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail = "User not found")
        else:
            return user
        
app.include_router(auth_router)
app.include_router(user_router)