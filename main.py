from zenml.client import Client
from pipeline.training_pipeline import model_training_pipeline
from utils.data_generator import insert_sample_data, add_daily_data

def setup_zenml():
    try:
        client = Client()
        print("ZenML client initialized")
    except Exception as e:
        print(f"Error initializing ZenML: {e}")
        print("Run 'zenml init' first")

def run_initial_setup():
    print("Setting up initial data...")
    insert_sample_data()
    print("Running initial training pipeline...")
    pipeline = model_training_pipeline()
   
