from fastapi import Depends, HTTPException, status, Header
from sqlmodel import Session
from ..core.db import get_session
from ..core.security import decode_token_header
from ..models.user import User

def get_db() -> Session:
    return next(get_session())

def get_current_user(authorization: str | None = Header(default=None), db: Session = Depends(get_db)) -> User:
    token = decode_token_header(authorization)
    # MVP: if no token, fall back to user id 1 for quick testing.
    user = db.get(User, token.sub) if token else db.get(User, 1)
    if not user:
        # create a default user for quick start
        user = User(id=1, email="demo@example.com", password_hash="demo")
        db.add(user); db.commit()
    return user

def pagination_params(limit: int = 20, offset: int = 0):
    return {"limit": max(1, min(limit, 100)), "offset": max(0, offset)}
