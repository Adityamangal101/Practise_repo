from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "test1234"
        }
    )

    assert response.status_code == 201
    assert "message" in response.json()

def test_login_user():
    response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "password": "test1234"
        }
    )

    assert response.status_code == 200
    assert "message" in response.json()

def test_login_wrong_password():
    response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "password": "wrongpass"
        }
    )

    assert response.status_code == 401
