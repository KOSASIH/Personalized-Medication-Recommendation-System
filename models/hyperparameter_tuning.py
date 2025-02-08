# hyperparameter_tuning.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

def tune_hyperparameters():
    # Load processed patient data
    data = pd.read_csv('data/processed/processed_patient_data.csv')
    target = data['medication']  # Assuming 'medication' is the target column
    features = data.drop(columns=['medication', 'patient_id'])  # Drop non-feature columns

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Define the model
    model = RandomForestClassifier(random_state=42)

    # Define the hyperparameter grid
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 3, 5]
    }

    # Initialize GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # # Get the best parameters and score
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    print(f"Best Parameters: {best_params}")
    print(f"Best Cross-Validation Score: {best_score}")

    # Save the best model
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, 'models/best_medication_model.pkl')
    print("Best model trained and saved as 'models/best_medication_model.pkl'.")

if __name__ == "__main__":
    tune_hyperparameters()
