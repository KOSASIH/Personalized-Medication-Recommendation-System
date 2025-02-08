# models/medication_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

class MedicationModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, data, target):
        """Train the medication recommendation model."""
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def predict(self, features):
        """Make predictions using the trained model."""
        return self.model.predict(features)

    def save_model(self, filepath):
        """Save the trained model to a file."""
        joblib.dump(self.model, filepath)

    def load_model(self, filepath):
        """Load a trained model from a file."""
        self.model = joblib.load(filepath)
