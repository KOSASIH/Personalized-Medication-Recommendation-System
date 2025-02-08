const API_BASE_URL = 'http://localhost:5000/api'; // Update with your backend URL

export const fetchRecommendations = async (patientId) => {
    const response = await fetch(`${API_BASE_URL}/recommendations`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ patient_id: patientId }),
    });
    if (!response.ok) {
        throw new Error('Failed to fetch recommendations');
    }
    return await response.json();
};

export const submitFeedback = async (feedbackData) => {
    const response = await fetch(`${API_BASE_URL}/feedback`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(feedbackData),
    });
    if (!response.ok) {
        throw new Error('Failed to submit feedback');
    }
    return await response.json();
};
