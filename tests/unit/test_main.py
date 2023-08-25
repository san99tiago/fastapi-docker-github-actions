from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello by Santi"}


def test_read_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
