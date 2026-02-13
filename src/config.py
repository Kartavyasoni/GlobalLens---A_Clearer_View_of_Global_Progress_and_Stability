### CONFIGURATION SETTINGS ###
# This file contains configuration settings for the project.


# World Bank API base URL
WORLD_BANK_API_URL = "https://api.worldbank.org/v2"

# API Parameters
API_PARAMS = {
    "format": "json",
    "per_page": 100, # Number of records per page
    "date": "2000:2026" # Date range for data
}

# Data Paths
DATA_PATHS = {
    "raw": "data/raw",
    "processed": "data/processed",
    "features": "data/features",
    "forecasts": "data/forecasts"
}

# Logging Path
LOGGING_PATH = "logs/gderis.log"