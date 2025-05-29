import schedule
import time
import subprocess
import sys

def run_pipeline():
    print("Running the training pipeline...")
    subprocess.run([sys.executable, "pipeline/training_pipeline.py"])

schedule.every(2).minutes.do(run_pipeline)

print("Scheduler started. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
