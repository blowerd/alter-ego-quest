from fastapi import APIRouter

router = APIRouter()

@router.post("/start")
def start_timer(skill_id: int):
    return {"status": "started", "skill_id": skill_id}

@router.post("/stop")
def stop_timer():
    return {"status": "stopped"}
