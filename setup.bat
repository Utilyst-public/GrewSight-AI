@echo off
echo ================================================
echo CrewSight-AI Setup
echo (c) 2025 Utilyst Inc. All rights reserved.
echo ================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Install Python 3.11+
    pause
    exit /b 1
)

python --version
echo.

if exist venv (
    echo [WARNING] venv exists.
) else (
    python -m venv venv
    echo [OK] venv created
)
echo.

call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo [OK] Dependencies installed
echo.

if exist .env (
    echo [WARNING] .env exists.
) else (
    copy .env.example .env >nul
    echo [OK] .env created
    echo.
    echo [IMPORTANT] Edit .env with your API keys!
)
echo.

if not exist downloads mkdir downloads
if not exist output mkdir output
echo [OK] Directories created
echo.

echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env with your API keys
echo 2. Run: venv\Scripts\activate
echo 3. Run: python -m src.crewsight.main
echo.
pause
