import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"

def test_login_user():
    response = client.post("/auth/login", json={
        "email": "admin@filament.com",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()