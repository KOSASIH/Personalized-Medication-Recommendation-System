# tests/backend/test_services.py

import pytest
from services.fhir_service import FHIRService
from services.recommendation_service import RecommendationService
from fhirclient import client

@pytest.fixture
def fhir_client():
    fhir_settings = {
        'app_id': 'your_app_id',
        'api_base': 'https://your.fhir.server/baseR4',
    }
    return client.FHIRClient(settings=fhir_settings)

def test_get_patient_data(fhir_client):
    """Test fetching patient data from FHIR."""
    fhir_service = FHIRService(fhir_client)
    patient_data = fhir_service.get_patient_data('1')  # Replace with a valid patient ID
    assert patient_data is not None
    assert 'id' in patient_data

def test_generate_recommendations(fhir_client):
    """Test generating medication recommendations."""
    fhir_service = FHIRService(fhir_client)
    recommendation_service = RecommendationService(None, None)  # Pass actual models if needed
    patient_data = fhir_service.get_patient_data('1')  # Replace with a valid patient ID
    recommendations = recommendation_service.generate_recommendations(patient_data)
    assert isinstance(recommendations, list)
