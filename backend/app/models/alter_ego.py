from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class AlterEgo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    name: str
    archetype: str | None = None
    backstory: str | None = None
    strengths: str | None = None
    constraints: str | None = None
    triggers: str | None = None
    color_hex: str | None = "#7c3aed"
    created_at: datetime = Field(default_factory=datetime.utcnow)
