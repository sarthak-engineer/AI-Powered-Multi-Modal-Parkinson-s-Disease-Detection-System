$projectRoot = $PSScriptRoot

# Activate the virtual environment
. "$projectRoot\venv\Scripts\Activate.ps1"

# Start the backend server in a new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd `"$projectRoot\app`"; uvicorn app:app --reload"

# Wait for a few seconds to let the backend start
Start-Sleep -Seconds 5

# Start the frontend
streamlit run "$projectRoot\streamlit\main.py"