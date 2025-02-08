import React from 'react';

const RecommendationCard = ({ recommendation }) => {
    return (
        <div className="recommendation-card">
            <h3>{recommendation.medication}</h3>
            <p>{recommendation.reason}</p>
            <p><strong>Dosage:</strong> {recommendation.dosage}</p>
        </div>
    );
};

export default RecommendationCard;
