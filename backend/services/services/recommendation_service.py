import numpy as np

class RecommendationService:
    def __init__(self, medication_model, sentiment_model):
        self.medication_model = medication_model
        self.sentiment_model = sentiment_model

    def generate_recommendations(self, patient_data):
        """Generate medication recommendations based on patient data."""
        # Extract relevant features from patient_data
        features = self.extract_features(patient_data)
        recommendations = self.medication_model.predict(features)
        return recommendations.tolist()

    def analyze_sentiment(self, review_text):
        """Analyze sentiment of the provided review text."""
        sentiment = self.sentiment_model.predict([review_text])
        return 'positive' if sentiment[0] == 1 else 'negative'

    def extract_features(self, patient_data):
        """Extract features from patient data for model input."""
        # Implement feature extraction logic based on patient_data
        # This is a placeholder for actual feature extraction
        return np.array([patient_data['age'], patient_data['condition']])
