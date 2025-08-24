from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .api.router import api_router
from .core.db import init_db

app = FastAPI(title="Alter Ego Quest", version="0.1.0")

# Mount static assets (CSS, icons, etc.)
app.mount("/static", StaticFiles(directory="backend/app/static"), name="static")
templates = Jinja2Templates(directory="backend/app/templates")

# Include versioned API
app.include_router(api_router, prefix="/api")

# Simple dashboard (optional)
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Alter Ego Quest"})

# Ensure tables exist once the app is fully imported (models included)
@app.on_event("startup")
def on_startup():
    init_db()
