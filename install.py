"""
    Running this script will download the NIH Chest X-ray dataset.
    You will need to set up your Kaggle API key.

    See: https://www.kaggle.com/datasets/nih-chest-xrays/data/code
    For API key see: https://www.kaggle.com/docs/api#authentication
"""

import kagglehub

# Change this to set path
PATH = "~/datasets"

# Download latest version
path = kagglehub.dataset_download("nih-chest-xrays/data", path=PATH)

print("Path to dataset files:", path)