import sys
import os

# Ajouter le dossier `/app` au chemin d'import
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from backend_api import app  

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test si l'API répond"""
    response = client.get("/")
    assert response.status_code == 200

#test_prediction
def test_prediction(client):
    """Test si l'API de prédiction fonctionne"""
    payload = {
        "order_requests": 10,
        "city_x": "amsterdam",
        "date": 10,
        "language": 1,
        "mobile": 0,
        "stock": 10,
        "group": 1,
        "brand": 1,
        "parking": 0,
        "pool": 0,
        "children_policy": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json
