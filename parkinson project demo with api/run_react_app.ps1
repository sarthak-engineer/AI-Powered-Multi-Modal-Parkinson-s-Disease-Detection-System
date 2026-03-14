$projectRoot = $PSScriptRoot

# Start Backend
Write-Host "Starting Backend Server..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot'; .\venv\Scripts\Activate.ps1; cd app; uvicorn app:app --reload"

# Wait a moment for backend to initialize
Start-Sleep -Seconds 2

# Start Frontend
Write-Host "Starting Frontend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot\frontend'; npm run dev"

Write-Host "Launched Backend and Frontend in separate windows."
