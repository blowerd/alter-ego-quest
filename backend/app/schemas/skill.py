from pydantic import BaseModel

class SkillCreate(BaseModel):
    name: str
    description: str | None = None
    color_hex: str | None = "#10b981"

class SkillOut(BaseModel):
    id: int
    name: str
    description: str | None
    color_hex: str | None
    class Config: 
        from_attributes = True

class SkillProgress(BaseModel):
    skill_id: int
    total_minutes: int
    level: int
    xp: int
    current_level_floor: int
    next_level_req: int
    to_next: int
    pct: float
