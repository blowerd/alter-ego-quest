import random
from typing import List, Optional

def roll_quest(templates, alter_ego_tags: List[str], skill_name: Optional[str] = None):
    def tagset(csv):
        return set(map(str.strip, csv.split(','))) if csv else set()

    candidates = [
        t for t in templates
        if (skill_name and t.skill_hint and t.skill_hint.lower() == skill_name.lower())
           or (t.tags_csv and tagset(t.tags_csv) & set(alter_ego_tags))
    ] or list(templates)

    t = random.choice(candidates) if candidates else None
    if not t:
        return {"title": "Free Study", "description": "Pick a related micro-task.", "minutes_estimate": 25, "template_id": None}
    est = random.randint(t.min_minutes, t.max_minutes)
    return {"title": t.title, "description": t.description, "minutes_estimate": est, "template_id": t.id}
