import os, time, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET = os.getenv("SECRET_KEY", "change-me")
ALGO = "HS256"
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p: str) -> str: 
    return pwd.hash(p)

def verify_password(p: str, h: str) -> bool: 
    return pwd.verify(p, h)

class TokenSub(BaseModel):
    sub: int  # user id

def create_token(user_id: int, ttl=60*60*24*7):
    now = int(time.time())
    return jwt.encode({"sub": user_id, "iat": now, "exp": now + ttl}, SECRET, algorithm=ALGO)

def decode_token_header(auth_header: str | None):
    if not auth_header or not auth_header.lower().startswith("bearer "):
        return None
    token = auth_header.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        return TokenSub(sub=payload.get("sub", 0))
    except Exception:
        return None
