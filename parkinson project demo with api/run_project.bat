@echo off
REM Activate the virtual environment
call venv\Scripts\activate

REM Navigate to the backend directory and start the backend server
cd app
uvicorn app:app --reload

REM Navigate back to the main directory and start the frontend
cd ..
start cmd /k "streamlit run streamlit/main.py"

REM Pause to keep the batch window open
pause
