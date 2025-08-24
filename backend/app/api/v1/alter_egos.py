from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ...models.alter_ego import AlterEgo
from ..deps import get_db, get_current_user

router = APIRouter()

@router.get("")
def list_egos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.exec(select(AlterEgo).where(AlterEgo.user_id==user.id)).all()

@router.post("")
def create_ego(payload: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ego = AlterEgo(user_id=user.id, **payload)
    db.add(ego); db.commit(); db.refresh(ego)
    return ego
