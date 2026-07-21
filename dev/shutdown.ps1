Write-Host "Stopping FastAPI..."

Get-Process python -ErrorAction SilentlyContinue |
    Where-Object {
        $_.Path -like "*IT-Career-Agent*"
    } |
    Stop-Process -Force

Write-Host ""
Write-Host "Development session stopped."