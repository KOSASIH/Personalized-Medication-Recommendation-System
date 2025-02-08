# run.py

from flask import Flask
from config import DevelopmentConfig
from utils.logging import setup_logging
from app import app  # Assuming your main app is defined in app.py

# Set up logging
setup_logging()

# Configure the app
app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
