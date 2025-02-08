import pandas as pd

# Load raw data
patient_data = pd.read_csv('data/raw/patient_data.csv')
medication_data = pd.read_csv('data/raw/medication_data.csv')
reviews = pd.read_csv('data/raw/reviews.csv')

# Process patient data
# Example: One-hot encoding for conditions
patient_data = pd.get_dummies(patient_data, columns=['condition'], drop_first=True)

# Save processed patient data
patient_data.to_csv('data/processed/processed_patient_data.csv', index=False)

# Process reviews
# Example: Lowercasing the review text
reviews['review_text'] = reviews['review_text'].str.lower()

# Save processed reviews
reviews.to_csv('data/processed/processed_reviews.csv', index=False)

# Process medication data if necessary
# For this example, we will just save it as is
medication_data.to_csv('data/processed/processed_medication_data.csv', index=False)

print("Data processing complete. Processed files saved in the 'data/processed/' directory.")
