# backend/tests/test_health.py
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/api/v1/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
