from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    name: str
    description: str | None = None
    color_hex: str | None = "#10b981"
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SkillLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    skill_id: int = Field(foreign_key="skill.id")
    started_at: datetime
    ended_at: datetime
    minutes: int
    source: str = "manual"  # or "timer"
