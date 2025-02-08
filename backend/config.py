# config.py

import os

class Config:
    """Base configuration."""
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    FHIR_APP_ID = os.getenv('FHIR_APP_ID', 'your_app_id')
    FHIR_API_BASE = os.getenv('FHIR_API_BASE', 'https://your.fhir.server/baseR4')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')

# You can extend this class for different environments (e.g., Development, Production)
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
