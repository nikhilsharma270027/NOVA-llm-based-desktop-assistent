@echo off
title Nova Agent

echo Starting Nova System...

REM Check if venv exists
if not exist venv (
    echo Virtual environment not found.
    echo Please run setup.bat first.
    pause
    exit /b
)

REM Activate environment
call venv\Scripts\activate

echo Bot is running. Press Ctrl+C to stop.
python -m nova.agents.telegram

pause
