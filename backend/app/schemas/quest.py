from pydantic import BaseModel
from typing import List, Optional

class QuestRollIn(BaseModel):
    alter_ego_id: int
    skill_id: Optional[int] = None
    skill_name: Optional[str] = None
    alter_ego_tags: List[str] = []

class QuestOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    minutes_estimate: int
    class Config:
        from_attributes = True
