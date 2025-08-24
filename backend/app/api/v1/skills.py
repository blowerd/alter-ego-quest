from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from ...models.skill import Skill, SkillLog
from ...schemas.skill import SkillCreate, SkillOut, SkillProgress
from ...services.leveling import next_level_progress
from ..deps import get_db, get_current_user, pagination_params

router = APIRouter()

@router.get("", response_model=list[SkillOut])
def list_skills(p=Depends(pagination_params), db: Session = Depends(get_db), user=Depends(get_current_user)):
    rows = db.exec(select(Skill).where(Skill.user_id == user.id).offset(p["offset"]).limit(p["limit"])).all()
    return rows

@router.post("", response_model=SkillOut, status_code=201)
def create_skill(payload: SkillCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    s = Skill(user_id=user.id, **payload.dict())
    db.add(s); db.commit(); db.refresh(s)
    return s

@router.get("/{skill_id}/progress", response_model=SkillProgress)
def skill_progress(skill_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    logs = db.exec(select(SkillLog).where(SkillLog.user_id==user.id, SkillLog.skill_id==skill_id)).all()
    total = sum(l.minutes for l in logs)
    prog = next_level_progress(total)
    return SkillProgress(skill_id=skill_id, total_minutes=total, **prog)
