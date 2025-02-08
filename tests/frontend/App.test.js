// tests/frontend/App.test.js

import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders medication recommendations heading', () => {
    render(<App />);
    const headingElement = screen.getByText(/Medication Recommendations/i);
    expect(headingElement).toBeInTheDocument();
});
