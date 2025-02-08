# tests/backend/test_medication.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_recommendations(client):
    """Test the recommendations endpoint."""
    response = client.post('/api/recommendations', json={'patient_id': '1'})
    assert response.status_code == 200
    assert 'medication' in response.get_json()[0]

def test_submit_feedback(client):
    """Test the feedback submission endpoint."""
    response = client.post('/api/feedback', json={'patient_id': '1', 'feedback': 'Great service!'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Feedback submitted successfully'
