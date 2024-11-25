import requests
import pytest
import json

BASE_URL = "https://petstore.swagger.io/v2"

def test_get_pets_by_status():
    """Test for retrieving pets by status"""
    status = "available"
    response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    assert len(pets) > 0
    for pet in pets:
        assert pet["status"] == status

def test_post_new_pet():
    """Test for adding a new pet"""
    pet_data = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Popin",
        "photoUrls": ["http://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    pet = response.json()
    print("json de respuesta" +json.dumps(pet))
    assert pet["name"] == "Popin"
    assert pet["status"] == "available"

def test_get_pet_by_id():
    """Test for retrieving a pet by ID"""
    pet_id = 12345
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    pet = response.json()
    assert pet["id"] == pet_id
    assert pet["name"] == "Popin"


