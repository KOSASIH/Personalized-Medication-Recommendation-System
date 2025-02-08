# API Documentation for Personalized Medication Recommendation System

## Overview

This document provides details about the API endpoints available in the Personalized Medication Recommendation System. The API is built using Flask and follows RESTful principles.

## Base URL

The base URL for the API is:

http://localhost:5000/api


## Endpoints

### 1. Get Medication Recommendations

- **Endpoint:** `/recommendations`
- **Method:** `POST`
- **Description:** Fetch personalized medication recommendations for a patient.
- **Request Body:**
    ```json
    {
        "patient_id": "string"
    }
    ```
- **Response:**
    - **Status Code:** `200 OK`
    - **Body:**
    ```json
    [
        {
            "medication": "string",
            "reason": "string",
            "dosage": "string"
        }
    ]
    ```
- **Example Request:**
    ```bash
    curl -X POST http://localhost:5000/api/recommendations -H "Content-Type: application/json" -d '{"patient_id": "1"}'
    ```

### 2. Submit Feedback

- **Endpoint:** `/feedback`
- **Method:** `POST`
- **Description:** Submit feedback on medication recommendations.
- **Request Body:**
    ```json
    {
        "patient_id": "string",
        "feedback": "string"
    }
    ```
- **Response:**
    - **Status Code:** `201 Created`
    - **Body:**
    ```json
    {
        "message": "Feedback submitted successfully"
    }
    ```
- **Example Request:**
    ```bash
    curl -X POST http://localhost:5000/api/feedback -H "Content-Type: application/json" -d '{"patient_id": "1", "feedback": "Great service!"}'
    ```

### 3. Analyze Sentiment

- **Endpoint:** `/sentiment`
- **Method:** `POST`
- **Description:** Analyze the sentiment of a medication review.
- **Request Body:**
    ```json
    {
        "review_text": "string"
    }
    ```
- **Response:**
    - **Status Code:** `200 OK`
    - **Body:**
    ```json
    {
        "sentiment": "positive" | "negative"
    }
    ```
- **Example Request:**
    ```bash
    curl -X POST http://localhost:5000/api/sentiment -H "Content-Type: application/json" -d '{"review_text": "This medication works great!"}'
    ```

## Error Handling

The API returns standard HTTP status codes to indicate the success or failure of a request. Common error responses include:

- **400 Bad Request:** The request was invalid or cannot be served.
- **404 Not Found:** The requested resource could not be found.
- **500 Internal Server Error:** An unexpected error occurred on the server.

## Authentication

Currently, the API does not require authentication. However, it is recommended to implement authentication for production use.

## Rate Limiting

There are no rate limits implemented on the API at this time. Consider implementing rate limiting to prevent abuse in a production environment.

## Contact

For any questions or issues, please contact the development team at [kosasihg88@gmail.com].
