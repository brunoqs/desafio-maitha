from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)

user_id = random.randint(1, 999999)

def test_create_user():
    sample_payload = {
        "id": user_id,
        "username": "PLACEHOLDER",
        "email": "PLACEHOLDER",
        "full_name": "PLACEHOLDER"
    }
    response = client.post("/users/", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == sample_payload


def test_get_user():
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": user_id,
        "username": "PLACEHOLDER",
        "email": "PLACEHOLDER",
        "full_name": "PLACEHOLDER"
    }


def test_update_user():
    sample_payload = {
        "id": user_id,
        "username": "PLACEHOLDER2",
        "email": "PLACEHOLDER2",
        "full_name": "PLACEHOLDER"
    }
    response = client.put(f"/users/{user_id}", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == sample_payload


def test_delete_user():
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200


def test_get_user_not_found():
    response = client.get(
        f"/users/0"
    )  # int not in DB
    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }
