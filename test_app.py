import pytest
from app import app, add_numbers

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_numbers_success():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(1.5, 2.5) == 4.0

def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers("2", 3)
    with pytest.raises(TypeError):
        add_numbers(2, None)

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'running' in data['message']

def test_add_route_success(client):
    response = client.get('/add?a=10&b=20')
    assert response.status_code == 200
    data = response.get_json()
    assert data['a'] == 10.0
    assert data['b'] == 20.0
    assert data['result'] == 30.0

def test_add_route_missing_parameters(client):
    response = client.get('/add?a=10')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'Missing parameters' in data['error']

def test_add_route_invalid_parameters(client):
    response = client.get('/add?a=ten&b=20')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'must be numeric' in data['error']
