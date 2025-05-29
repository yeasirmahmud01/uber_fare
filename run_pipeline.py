import os
import subprocess

def run_pipeline():
    print("Running the training pipeline...")

    # Get the path to the current venv python executable
    python_executable = os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe')
    
    subprocess.run([python_executable, "pipeline/training_pipeline.py"])
