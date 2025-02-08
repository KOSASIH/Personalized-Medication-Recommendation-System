# evaluate_model.py

import pandas as pd
from sklearn.metrics import classification_report
import joblib

def evaluate_medication_model():
    # Load the trained model
    model = joblib.load('models/medication_model.pkl')

    # Load new data for evaluation
    data = pd.read_csv('data/processed/processed_patient_data.csv')
    target = data['medication']  # Assuming 'medication' is the target column
    features = data.drop(columns=['medication', 'patient_id'])  # Drop non-feature columns

    # Make predictions
    predictions = model.predict(features)

    # Evaluate the model
    print(classification_report(target, predictions))

if __name__ == "__main__":
    evaluate_medication_model()
