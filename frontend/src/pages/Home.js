import React, { useEffect, useState } from 'react';
import RecommendationCard from '../components/RecommendationCard';
import FeedbackForm from '../components/FeedbackForm';
import { fetchRecommendations, submitFeedback } from '../services/apiService';

const Home = () => {
    const [recommendations, setRecommendations] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            const data = await fetchRecommendations('patient_id'); // Replace with actual patient ID
            setRecommendations(data);
            setLoading(false);
        };
        fetchData();
    }, []);

    const handleFeedbackSubmit = async (feedback) => {
        await submitFeedback({ feedback, patient_id: 'patient_id' }); // Replace with actual patient ID
        alert('Feedback submitted successfully!');
    };

    return (
        <div>
            <h1>Medication Recommendations</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                recommendations.map((rec, index) => (
                    <RecommendationCard key={index} recommendation={rec} />
                ))
            )}
            <FeedbackForm onSubmit={handleFeedbackSubmit} />
        </div>
    );
};

export default Home;
