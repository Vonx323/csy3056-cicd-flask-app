import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Welcome to the CSY3056 Flask App!"

def test_greet(client):
    response = client.get('/greet/Alex')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, Alex!"

def test_add(client):
    response = client.post('/add', json={'a': 5, 'b': 7})
    assert response.status_code == 200
    assert response.json['result'] == 12