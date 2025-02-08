import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Home} />
                {/* Add more routes as needed */}
            </Switch>
        </Router>
    );
};

export default App;
