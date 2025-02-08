<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/KOSASIH/Personalized-Medication-Recommendation-System">MediPredictor</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.linkedin.com/in/kosasih-81b46b5a">KOSASIH</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

# Personalized-Medication-Recommendation-System
The Personalized Medication Recommendation System is an AI-driven application that provides tailored medication suggestions for patients based on their unique health profiles. By integrating with Electronic Health Records (EHR) using the SMART on FHIR standard, this system analyzes patient data—including demographics, medical history, and current medications—to deliver accurate and personalized recommendations. Utilizing advanced machine learning algorithms, the app aims to assist healthcare providers in making informed medication decisions, improving patient outcomes, and enhancing overall treatment efficacy. The repository includes the complete codebase, model training scripts, and documentation for deployment and usage.

# Personalized Medication Recommendation System

## Overview

The **Personalized Medication Recommendation System** is an AI-driven application designed to provide tailored medication suggestions for patients based on their unique health profiles. By integrating with Electronic Health Records (EHR) using the SMART on FHIR standard, this system analyzes patient data—including demographics, medical history, and current medications—to deliver accurate and personalized recommendations. The application aims to assist healthcare providers in making informed medication decisions, improving patient outcomes, and enhancing overall treatment efficacy.

## Features

- **Personalized Medication Recommendations:** Provides tailored medication suggestions based on patient data.
- **EHR Integration:** Seamlessly integrates with EHR systems using the SMART on FHIR standard.
- **User  Feedback:** Allows healthcare providers to submit feedback on recommendations.
- **Sentiment Analysis:** Analyzes patient reviews to gauge sentiment towards medications.
- **User -Friendly Interface:** Intuitive and responsive design for easy navigation.

## Tech Stack

- **Backend:** Flask, FHIR Client, Scikit-learn, Joblib, Pandas, NumPy
- **Frontend:** React, React Router
- **Database:** PostgreSQL or MongoDB (if applicable)
- **Deployment:** Docker (optional), Heroku, AWS, or any cloud service

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL or MongoDB (if applicable)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/KOSASIH/Personalized-Medication-Recommendation-System.git
   cd Personalized-Medication-Recommendation-System/backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application settings in `config.py`:

   - Set your FHIR app ID and API base URL.
   - Adjust any other settings as needed.

5. Run the backend server:

   ```bash
   python run.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install the required Node.js packages:

   ```bash
   npm install
   ```

3. Start the frontend application:

   ```bash
   npm start
   ```

4. Open your browser and go to `http://localhost:3000`.

## Usage

1. **Access the Application:** Open your web browser and navigate to `http://localhost:3000`.
2. **View Recommendations:** The home page will display personalized medication recommendations based on the patient data fetched from the backend.
3. **Submit Feedback:** Use the feedback form to submit your thoughts on the recommendations provided.

## API Endpoints

### Recommendations

- **Endpoint:** `/api/recommendations`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "patient_id": "string"
    }
    ```
- **Response:**
    ```json
    [
        {
            "medication": "string",
            "reason": "string",
            "dosage": "string"
        }
    ]
    ```

### Feedback

- **Endpoint:** `/api/feedback`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "patient_id": "string",
        "feedback": "string"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Feedback submitted successfully"
    }
    ```

### Sentiment Analysis

- **Endpoint:** `/api/sentiment`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "review_text": "string"
    }
    ```
- **Response:**
    ```json
    {
        "sentiment": "positive" | "negative"
    }
    ```

## Future Enhancements

- Integration of real-time patient monitoring data to refine recommendations.
- Expansion of the model to include additional therapeutic areas and medication classes.
- Development of a mobile application for on-the-go access to recommendations and patient data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)
- [SMART on FHIR](https://smarthealthit.org/) for providing a framework for integrating with EHR systems.  
- [Scikit-learn](https://scikit-learn.org/) for machine learning capabilities.  
- [PostgreSQL](https://www.postgresql.org/) or [MongoDB](https://www.mongodb.com/) for database management.  
- All contributors and supporters of the project.  

## Contact

For any inquiries or feedback, please reach out to the project maintainer at [kosasihg88@gmail.com].
