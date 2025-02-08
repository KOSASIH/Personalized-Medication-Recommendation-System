from flask import Flask, request, jsonify
from flask_cors import CORS
from fhirclient import client
from fhirclient.models import patient, medicationrequest
import joblib
import logging
from services.fhir_service import FHIRService
from services.recommendation_service import RecommendationService

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FHIR Client Configuration
fhir_settings = {
    'app_id': 'your_app_id',
    'api_base': 'https://your.fhir.server/baseR4',
}
fhir_client = client.FHIRClient(settings=fhir_settings)

# Load machine learning models
medication_model = joblib.load('models/medication_model.pkl')
sentiment_model = joblib.load('models/sentiment_analysis_model.pkl')

# Initialize services
fhir_service = FHIRService(fhir_client)
recommendation_service = RecommendationService(medication_model, sentiment_model)

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """Endpoint to get personalized medication recommendations."""
    data = request.json
    patient_id = data.get('patient_id')

    # Fetch patient data from FHIR
    patient_data = fhir_service.get_patient_data(patient_id)
    if not patient_data:
        return jsonify({'error': 'Patient not found'}), 404

    # Generate recommendations
    recommendations = recommendation_service.generate_recommendations(patient_data)
    return jsonify(recommendations), 200

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """Endpoint to submit user feedback on recommendations."""
    data = request.json
    feedback = data.get('feedback')
    patient_id = data.get('patient_id')

    # Process feedback (e.g., store in a database or log)
    logger.info(f"Feedback received from patient {patient_id}: {feedback}")
    # Here you would typically save the feedback to a database

    return jsonify({'message': 'Feedback submitted successfully'}), 201

@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():
    """Endpoint to analyze sentiment of medication reviews."""
    data = request.json
    review_text = data.get('review_text')

    # Analyze sentiment
    sentiment = recommendation_service.analyze_sentiment(review_text)
    return jsonify({'sentiment': sentiment}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
