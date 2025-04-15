
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Ласкаво просимо!"}

def test_create_item():
    test_item = {
        "id": "test-item-1",
        "name": "Тестовий товар",
        "description": "Опис тестового товару",
        "price": 100.0,
        "is_available": True
    }
    response = client.post("/items/", json=test_item)
    assert response.status_code == 201
    assert response.json() == test_item

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1

def test_read_item():
    test_item = {
        "id": "test-item-2",
        "name": "Другий тестовий товар",
        "description": "Опис другого тестового товару",
        "price": 200.0,
        "is_available": True
    }
    client.post("/items/", json=test_item)
    
    response = client.get(f"/items/{test_item['id']}")
    assert response.status_code == 200
    assert response.json() == test_item

def test_update_item():
    test_item = {
        "id": "test-item-3",
        "name": "Товар для оновлення",
        "description": "Опис товару для оновлення",
        "price": 300.0,
        "is_available": True
    }
    client.post("/items/", json=test_item)
    
    updated_item = test_item.copy()
    updated_item["name"] = "Оновленний товар"
    updated_item["price"] = 350.0
    
    response = client.put(f"/items/{test_item['id']}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == updated_item
    
    check_response = client.get(f"/items/{test_item['id']}")
    assert check_response.json() == updated_item

def test_delete_item():
    test_item = {
        "id": "test-item-4",
        "name": "Товар для видаления",
        "description": "Цей товар буде видалений",
        "price": 400.0,
        "is_available": True
    }
    client.post("/items/", json=test_item)
    
    response = client.delete(f"/items/{test_item['id']}")
    assert response.status_code == 204
    
    check_response = client.get(f"/items/{test_item['id']}")
    assert check_response.status_code == 404

def test_get_nonexistent_item():
    response = client.get("/items/non-existent-id")
    assert response.status_code == 404
    assert "detail" in response.json()
