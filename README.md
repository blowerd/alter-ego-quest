# Alter Ego Quest (MVP)

Self-hosted MVP in Python/FastAPI for identity-first habit building with time-based leveling.

## Quick start
```bash
docker compose up --build
# then visit http://localhost:8000/docs
```

## API
- Versioned under `/api/v1`
- Health: `/api/v1/healthz`
- Auth: `/api/v1/auth/register`, `/api/v1/auth/login`
- Skills: `/api/v1/skills`, `/api/v1/skills/{id}/progress`
- Quests: `/api/v1/quests/roll`, `/api/v1/quests/{id}/complete`

## Notes
- Auth is minimal; for local play it defaults to a demo user if no token is provided.
- DB is SQLite stored in the `data/` volume.
- Templates and CSS are stubs—edit `backend/app/templates/` and `backend/app/static/styles.css`.
