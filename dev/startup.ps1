Write-Host ""
Write-Host "================================="
Write-Host " IT Career Agent Startup"
Write-Host "================================="
Write-Host ""

Set-Location "$PSScriptRoot\.."

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host ""
Write-Host "Ollama Models:"
ollama list

Write-Host ""
Write-Host "Starting FastAPI..."
Start-Process powershell `
    -ArgumentList "-NoExit","-Command",". .\.venv\Scripts\Activate.ps1; uvicorn app.api.main:app --reload"

Start-Sleep 2

Start-Process "http://127.0.0.1:8000/docs"

Write-Host ""
Write-Host "Swagger:"
Write-Host "http://127.0.0.1:8000/docs"
Write-Host ""
Write-Host "Ready!"