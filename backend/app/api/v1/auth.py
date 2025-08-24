from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ...core.security import hash_password, verify_password, create_token
from ...models.user import User
from ...schemas.auth import RegisterIn, LoginIn, TokenOut
from ..deps import get_db

router = APIRouter()

@router.post("/register", response_model=TokenOut)
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    existing = db.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    u = User(email=payload.email, password_hash=hash_password(payload.password))
    db.add(u); db.commit(); db.refresh(u)
    return TokenOut(access_token=create_token(u.id), token_type="bearer")

@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    u = db.exec(select(User).where(User.email == payload.email)).first()
    if not u or not verify_password(payload.password, u.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return TokenOut(access_token=create_token(u.id), token_type="bearer")
