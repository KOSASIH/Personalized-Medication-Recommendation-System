# utils/data_processing.py

import pandas as pd
import numpy as np

def preprocess_patient_data(patient_data):
    """
    Preprocess patient data for model input.
    
    Args:
        patient_data (dict): Raw patient data from FHIR.

    Returns:
        pd.DataFrame: Processed patient data ready for model input.
    """
    # Example preprocessing steps
    processed_data = {
        'age': patient_data.get('age', 0),
        'gender': 1 if patient_data.get('gender') == 'male' else 0,
        'condition': patient_data.get('condition', ''),
        'medications': patient_data.get('medications', []),
        # Add more features as needed
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([processed_data])
    
    # Handle categorical variables (e.g., one-hot encoding)
    df = pd.get_dummies(df, columns=['condition'], drop_first=True)
    
    return df

def preprocess_reviews(reviews):
    """
    Preprocess a list of reviews for sentiment analysis.
    
    Args:
        reviews (list): List of review texts.

    Returns:
        list: Preprocessed review texts.
    """
    # Example preprocessing steps
    processed_reviews = [review.lower() for review in reviews]  # Convert to lowercase
    # Add more preprocessing steps (e.g., removing punctuation, stop words)
    
    return processed_reviews
