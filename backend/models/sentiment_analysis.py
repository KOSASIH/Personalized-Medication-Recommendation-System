# models/sentiment_analysis.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import joblib

class SentimentAnalysisModel:
    def __init__(self):
        self.model = None

    def train(self, reviews, sentiments):
        """Train the sentiment analysis model."""
        X_train, X_test, y_train, y_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=42)
        self.model = make_pipeline(CountVectorizer(), LogisticRegression())
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def predict(self, review):
        """Make predictions using the trained model."""
        return self.model.predict([review])[0]

    def save_model(self, filepath):
        """Save the trained model to a file."""
        joblib.dump(self.model, filepath)

    def load_model(self, filepath):
        """Load a trained model from a file."""
        self.model = joblib.load(filepath)
