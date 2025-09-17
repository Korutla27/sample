import json
from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Welcome to Flask Sample App!"

def test_greet():
    client = app.test_client()
    res = client.get("/greet/ChatGPT")
    assert res.status_code == 200
    assert "ChatGPT" in res.get_json()["greeting"]

def test_add():
    client = app.test_client()
    res = client.post("/add", json={"a": 5, "b": 7})
    assert res.status_code == 200
    assert res.get_json()["result"] == 12
