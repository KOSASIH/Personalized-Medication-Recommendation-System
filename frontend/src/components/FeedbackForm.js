import React, { useState } from 'react';

const FeedbackForm = ({ onSubmit }) => {
    const [feedback, setFeedback] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(feedback);
        setFeedback('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea
                value={feedback}
                onChange={(e) => setFeedback(e.target.value)}
                placeholder="Provide your feedback here..."
                required
            />
            <button type="submit">Submit Feedback</button>
        </form>
    );
};

export default FeedbackForm;
