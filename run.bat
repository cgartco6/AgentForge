@echo off
REM AgentForge - AI Agent Ecosystem
REM For Windows 10/11 systems

echo Starting AgentForge ecosystem...

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install Python dependencies
echo Installing Python dependencies...
pip install -r backend\requirements.txt

REM Set environment variables
set FLASK_APP=backend\app.py
set FLASK_ENV=development

REM Start the backend server
echo Starting backend server...
start /B flask run --host=0.0.0.0 --port=5000

REM Wait for server to start
timeout /t 8 /nobreak >nul

REM Open the website in default browser
echo Opening AgentForge in your browser...
start http://localhost:5000

echo AgentForge is now running!
echo You can access the system at: http://localhost:5000
echo Press any key to stop the ecosystem...
pause >nul

REM Stop the server
taskkill /f /im python.exe >nul
echo Ecosystem stopped.
