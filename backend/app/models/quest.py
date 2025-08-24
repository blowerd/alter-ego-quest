from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class QuestTemplate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    difficulty: int = 1
    tags_csv: str | None = None
    skill_hint: str | None = None
    min_minutes: int = 25
    max_minutes: int = 60

class QuestInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    alter_ego_id: int = Field(foreign_key="alterego.id")
    skill_id: int | None = Field(default=None, foreign_key="skill.id")
    template_id: int | None = Field(default=None, foreign_key="questtemplate.id")
    title: str
    description: str
    status: str = "open"  # open|done|skipped
    minutes_estimate: int = 30
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None
