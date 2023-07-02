from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Mock user data for demonstration
users = [
    {"username": "user1", "password": pwd_context.hash("password1")},
    {"username": "user2", "password": pwd_context.hash("password2")},
]

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(username):
    payload = {"sub": username}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(username, password):
    user = next((user for user in users if user["username"] == username), None)
    if not user or not verify_password(password, user["password"]):
        return False
    return True

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user = next((user for user in users if user["username"] == username), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except (PyJWTError, StopIteration):
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
def login(username: str, password: str):
    if authenticate_user(username, password):
        access_token = create_access_token(username)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": f"Access granted for user: {user['username']}"}
