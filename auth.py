from fastapi import APIRouter, HTTPException, Depends, Header, FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
USERS = {"mitsu": pwd_ctx.hash("1234"), "lucas": pwd_ctx.hash("abcd")}
SECRET = "CHANGE_ME"
ALGO = "HS256"
ACCESS_MINUTES = 60

class LoginIn(BaseModel):
    username: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

def create_token(username: str) -> str:
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_MINUTES)}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def verify_token(token: str) -> str:
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@router.post("/login", response_model=TokenOut)
def login(body: LoginIn):
    hashed = USERS.get(body.username)
    if not hashed or not pwd_ctx.verify(body.password, hashed):
        raise HTTPException(status_code=401, detail="Bad credentials")
    return TokenOut(access_token=create_token(body.username))

@router.get("/me")
def me(authorization: str = Header(default="")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    username = verify_token(authorization.split(" ", 1)[1])
    return {"username": username}