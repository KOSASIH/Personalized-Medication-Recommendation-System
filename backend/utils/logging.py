# utils/logging.py

import logging

def setup_logging(log_file='app.log'):
    """
    Set up logging configuration.
    
    Args:
        log_file (str): The name of the log file.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("Logging is set up.")
