from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_application_startup_status():
    request = client.get("/")
    assert request.status_code == 200


def test_get_meme_from_empty_db():
    request = client.get("/memes/1")
    assert request.status_code == 404


def test_get_memes_paginated_empty_db():
    request = client.get("/memes/")
    assert request.json() == []
