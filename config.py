from pathlib import Path

# Database paths
DB_PATH = "data/training_data.db"
MODEL_REGISTRY_DB = "data/model_registry.db"

# Table names
DATA_TABLE = "training_data"
MODEL_TABLE = "models"  # Make sure this matches with your steps.py code

# Model evaluation thresholds
MAX_ALLOWED_MSE = 100.0
MIN_ALLOWED_R2 = 0.7

# Ensure required directories exist
Path("data").mkdir(exist_ok=True)
Path("models").mkdir(exist_ok=True)
