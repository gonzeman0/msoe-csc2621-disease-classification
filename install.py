"""
    Running this script will download the NIH Chest X-ray dataset.
    You will need to set up your Kaggle API key.

    See: https://www.kaggle.com/datasets/nih-chest-xrays/data/code
    For API key see: https://www.kaggle.com/docs/api#authentication
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path

# Set the dataset slug (from Kaggle URL)
DATASET = "nih-chest-xrays/data"  # Replace with any other slug if needed

# Set your download path (e.g., ~/datasets)
DOWNLOAD_PATH = Path("~/datasets").expanduser()
DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)  # Create it if it doesn't exist

# Initialize and authenticate
api = KaggleApi()
api.authenticate()

# Download and unzip dataset
api.dataset_download_files(dataset=DATASET, path=str(DOWNLOAD_PATH), unzip=True)

print(f"Dataset downloaded to: {DOWNLOAD_PATH}")

