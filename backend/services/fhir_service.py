from fhirclient.models import patient

class FHIRService:
    def __init__(self, fhir_client):
        self.fhir_client = fhir_client

    def get_patient_data(self, patient_id):
        """Fetch patient data from FHIR server."""
        try ```python
            patient_data = patient.Patient.read(patient_id, self.fhir_client)
            return patient_data.as_json() if patient_data else None
        except Exception as e:
            logger.error(f"Error fetching patient data: {e}")
            return None
