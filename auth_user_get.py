from fastapi import FastAPI,  HTTPException
from auth_model_users import User
from auth_user_connection import Session


app = FastAPI()


@app.get("/users/")
def get_user():
    with Session() as session:
        users = session.query(User).all()
        return users
    
@app.get("/users/{user_id}")
def get_user(user_id : int):
    with Session() as session:
    
        user = session.query(User).get(user_id)
        if user is None:
            raise HTTPException(status_code = 404, detail = "Users not found")
        return user
