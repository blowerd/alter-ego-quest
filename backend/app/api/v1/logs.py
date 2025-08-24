from datetime import datetime
from fastapi import APIRouter, Depends
from sqlmodel import Session
from ...models.skill import SkillLog
from ..deps import get_db, get_current_user

router = APIRouter()

@router.post("")
def create_log(skill_id: int, minutes: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    now = datetime.utcnow()
    log = SkillLog(user_id=user.id, skill_id=skill_id, started_at=now, ended_at=now, minutes=minutes, source="manual")
    db.add(log); db.commit(); db.refresh(log)
    return log
