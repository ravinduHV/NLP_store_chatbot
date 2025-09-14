
if (!(Test-Path env)) {
    Write-Host "Creating virtual environment..."
    python -m venv env
}

Write-Host "Activating virtual environment..."
& env\Scripts\Activate.ps1
Clear-Host

Write-Host "Installing requirements..."
pip install -r requirements.txt
Clear-Host

Write-Host "Running main.py..."
python main.py