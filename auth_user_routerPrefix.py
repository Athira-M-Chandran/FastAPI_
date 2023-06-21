from fastapi import FastAPI, HTTPException, APIRouter
from auth_model_users import User
from auth_user_connection import Session

auth_router = APIRouter(prefix= "/auth")
user_router = APIRouter(prefix = "/users")

app = FastAPI()

@auth_router.post("/login")
def login():
    # Authentication logic goes here
    pass

@user_router.get("/")
def get_all_users():
    with Session() as session:
        users = session.query(User).all()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return users
    
@user_router.get("/{user_id}")
def get_user(user_id: int):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
app.include_router(auth_router)
app.include_router(user_router)