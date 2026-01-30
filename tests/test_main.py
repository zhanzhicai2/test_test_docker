
import pytest
import requests


url = "http://47.101.36.103:8000"


def test_health_check():
    response = requests.get(f"{url}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# def test_create_item():
#     response = client.post(f"{url}/items/", json={"name": "Test Item", "description": "A test item", "price": 100})
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Test Item"
#     assert data["description"] == "A test item"
#     assert data["price"] == 100
#     assert "id" in data

# def test_read_item():
#     # First, create an item
#     response = client.post(f"{client.base_url}/items/", json={"name": "Test Item", "description": "A test item", "price": 100})
#     data = response.json()
#     item_id = data["id"]

#     # Then, read the item
#     response = client.get(f"{client.base_url}/items/{item_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Test Item"
#     assert data["description"] == "A test item"
#     assert data["price"] == 100

# def test_update_item():
#     # First, create an item
#     response = client.post(f"{client.base_url}/items/", json={"name": "Test Item", "description": "A test item", "price": 100})
#     data = response.json()
#     item_id = data["id"]

#     # Then, update the item
#     response = client.put(f"{client.base_url}/items/{item_id}", json={"name": "Updated Item", "description": "Updated description", "price": 200})
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Updated Item"
#     assert data["description"] == "Updated description"
#     assert data["price"] == 200