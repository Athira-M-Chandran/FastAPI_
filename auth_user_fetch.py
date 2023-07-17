from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth_user_connection import Session
from auth_model_users import User
from jwt import PyJWTError
import bcrypt
import datetime
import jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')


def authenticate_user(username : str, password : str):
    with Session() as session:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            return False
        if not bcrypt.checkpw(password.encode(),user.password.encode()):
            return False
        return user
    
def create_access_token(data : dict, secret_key : str, expires_delta : int):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes = expires_delta)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm='HS256')
    return encoded_jwt

@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user  = authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail= "Invalid username or password")
    access_token = create_access_token(data= {
        'sub': user.username
    }, secret_key='your_secret_key', expires_delta=30)
    return {'access_token' : access_token, 'token_type' : 'bearer'}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, 'your_secret_key',algorithms=['HS256'])
        username = payload.get('sub')
        if not username:
            raise HTTPException(status_code=401,detail='Invalid authentication token')
        with Session() as session:
            user = session.query(User).filter(User.username==username).first()
            if not user:
                raise HTTPException(status_code=401, detail="User not found")
        return user
    except PyJWTError:
        raise HTTPException(status_code=401, detail='Invalid authentication token')
    
@app.get('/protected')
def protected_route(user: User = Depends(get_current_user)):
    return {'username' : user.username, 'email' : user.email}


