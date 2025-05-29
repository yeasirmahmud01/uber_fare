@echo off
echo ================================================
echo 🚀 Launching ML Project with Environment Setup...
echo ================================================

REM Navigate to your project folder
cd /d "C:\Users\ASUS\ml_project"

REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip (optional)
echo 🔄 Upgrading pip...
python -m pip install --upgrade pip

REM Install required packages
echo 📦 Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Run the scheduler script
echo ⏰ Starting scheduler...
python scheduler.py

pause
