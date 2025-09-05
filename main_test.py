import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Load test data once
with open("data.json", "r") as f:
    test_data = json.load(f)


def test_read_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_data_by_guid():
    guid = test_data[0]["guid"]
    response = client.get(f"/{guid}")
    assert response.status_code == 200
    assert response.json() == test_data[0]


def test_read_data_by_invalid_guid():
    response = client.get("/invalid-guid")
    assert response.status_code == 404
