### DATA VALIDATION MODULE ###
# This module provides validation utilities for API responses.

def validate_api_response(response):
    """Validate the API response structure."""
    if not response or 'data' not in response:
        raise ValueError("Invalid API response structure.")