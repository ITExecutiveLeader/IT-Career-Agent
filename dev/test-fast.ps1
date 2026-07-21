Set-Location "$PSScriptRoot\.."

. .\.venv\Scripts\Activate.ps1

$env:MODEL_NAME="ollama/qwen2.5:7b"

pytest