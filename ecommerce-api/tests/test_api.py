import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
    with app.app_context():
        db.drop_all()

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200

def test_post_product(client):
    response = client.post('/products', json={"name": "Test Product", "description": "Description", "price": 10.0, "stock": 100})
    assert response.status_code == 201

def test_post_order_with_insufficient_stock(client):
    product_response = client.post('/products', json={"name": "Test Product", "description": "Description", "price": 10.0, "stock": 1})
    order_response = client.post('/orders', json={"products": [{"id": 1, "quantity": 2}]})
    assert order_response.status_code == 400
