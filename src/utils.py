### UTILITIES MODULE ###
# This module contains utility functions for file operations and data handling.


import os
import json
import logging
from pathlib import Path

# Utility functions for file operations and data handling
def read_json(file_path):
    """
    Reads a JSON file and returns the data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
        raise

# Directory management utility
def create_directory(dir_path):
    """
    Creates a directory if it does not exist.
    """
    try:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory created at: {dir_path}")
    except Exception as e:
        logging.error(f"Error creating directory {dir_path}: {e}")
        raise

# Data writing utility
def write_json(file_path, data):
    """
    Writes data to a JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data written to JSON file: {file_path}")
    except Exception as e:
        logging.error(f"Error writing to JSON file {file_path}: {e}")
        raise