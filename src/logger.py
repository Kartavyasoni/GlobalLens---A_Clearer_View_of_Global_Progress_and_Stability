### LOGGING SETUP ###
# This module sets up logging for the application, creating a logs directory

import logging
import os
from datetime import datetime

# Get today's date to create a folder for logs
today_date = datetime.now().strftime('%Y-%m-%d')

# Create a directory for today's logs
LOGS_DIR = os.path.join(os.getcwd(), "logs", today_date)
os.makedirs(LOGS_DIR, exist_ok=True)

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%H:%M:%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)