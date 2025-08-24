from fastapi import APIRouter
from .v1 import health, skills, quests, auth, users, alter_egos, logs, timers

api_router = APIRouter()
v1 = APIRouter(prefix="/v1")

v1.include_router(health.router, tags=["health"])
v1.include_router(auth.router, prefix="/auth", tags=["auth"])
v1.include_router(users.router, prefix="/users", tags=["users"])
v1.include_router(alter_egos.router, prefix="/alter-egos", tags=["alter-egos"])
v1.include_router(skills.router, prefix="/skills", tags=["skills"])
v1.include_router(logs.router, prefix="/logs", tags=["logs"])
v1.include_router(timers.router, prefix="/timers", tags=["timers"])
v1.include_router(quests.router, prefix="/quests", tags=["quests"])

api_router.include_router(v1)
