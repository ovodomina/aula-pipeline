# tests/test_app.py

import sys
import os
import pytest

# Adiciona o diretório pai ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.data == b'Hello, Flask!'
    assert response.status_code == 200
