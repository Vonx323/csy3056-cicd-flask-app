import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hello, World" in res.data

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert b"OK" in res.data

def test_invalid_route(client):
    res = client.get('/not-found')
    assert res.status_code == 404
