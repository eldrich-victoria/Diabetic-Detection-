import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "xception_dr.h5")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")

# Flask
SECRET_KEY = "change-this-secret-key"

# Image settings (Xception input)
IMAGE_SIZE = (299, 299)

# Ensure runtime folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
