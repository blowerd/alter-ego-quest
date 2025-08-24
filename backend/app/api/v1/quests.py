from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ...models.quest import QuestTemplate, QuestInstance
from ...schemas.quest import QuestRollIn, QuestOut
from ...services.quests import roll_quest
from ..deps import get_db, get_current_user

router = APIRouter()

@router.post("/roll", response_model=QuestOut)
def roll(payload: QuestRollIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    templates = db.exec(select(QuestTemplate)).all()
    result = roll_quest(templates, payload.alter_ego_tags, payload.skill_name)
    qi = QuestInstance(
        user_id=user.id,
        alter_ego_id=payload.alter_ego_id,
        skill_id=payload.skill_id,
        template_id=result.get("template_id"),
        title=result["title"],
        description=result["description"],
        minutes_estimate=result["minutes_estimate"]
    )
    db.add(qi); db.commit(); db.refresh(qi)
    return qi

@router.post("/{quest_id}/complete", response_model=QuestOut)
def complete(quest_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    qi = db.get(QuestInstance, quest_id)
    if not qi or qi.user_id != user.id:
        raise HTTPException(404, "Quest not found")
    qi.status = "done"
    db.add(qi); db.commit(); db.refresh(qi)
    return qi
