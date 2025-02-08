# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_medication_model():
    # Load processed patient data
    data = pd.read_csv('data/processed/processed_patient_data.csv')
    target = data['medication']  # Assuming 'medication' is the target column
    features = data.drop(columns=['medication', 'patient_id'])  # Drop non-feature columns

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    # Save the trained model
    joblib.dump(model, 'models/medication_model.pkl')
    print("Model trained and saved as 'models/medication_model.pkl'.")

if __name__ == "__main__":
    train_medication_model()
