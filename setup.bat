@echo off
setlocal EnableDelayedExpansion

cd /d "%~dp0"
title Nova Assistant Setup
color 0A
cls

echo =====================================
echo Nova Assistant - Setup Starting
echo =====================================

REM ---------------- STEP 1 ----------------
echo [1/6] Checking Python...

py -3.11 --version >nul 2>&1
if not errorlevel 1 (
    set "PYTHON_CMD=py -3.11"
    goto :FoundPython
)

for /f "tokens=2 delims= " %%v in ('python --version 2^>nul') do set CUR_VER=%%v

if "!CUR_VER:~0,4!"=="3.11" set "PYTHON_CMD=python" & goto :FoundPython
if "!CUR_VER:~0,4!"=="3.10" set "PYTHON_CMD=python" & goto :FoundPython
if "!CUR_VER:~0,4!"=="3.12" set "PYTHON_CMD=python" & goto :FoundPython

echo ERROR: Python 3.10+ not found.
pause
exit /b 1

:FoundPython
echo Python OK.

REM ---------------- STEP 2 ----------------
echo [2/6] Creating virtual environment...

if exist venv rmdir /s /q venv
%PYTHON_CMD% -m venv venv

if errorlevel 1 (
    echo Failed to create venv.
    pause
    exit /b 1
)

REM ---------------- STEP 3 ----------------
echo [3/6] Installing dependencies...

call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .

if errorlevel 1 (
    echo Package install failed.
    pause
    exit /b 1
)

REM ---------------- STEP 4 ----------------
echo [4/6] Checking Ollama model...

ollama list | findstr /i "qwen2.5-coder:7b" >nul
if errorlevel 1 (
    echo Downloading model...
    ollama pull qwen2.5-coder:7b
)

REM ---------------- STEP 5 ----------------
echo [5/6] Creating .env and silent launcher...

if not exist .env (
    echo TELEGRAM_TOKEN=PASTE_TOKEN_HERE> .env
    echo MODEL_NAME=qwen2.5-coder:7b>> .env
)

(
echo Set WshShell = CreateObject("WScript.Shell")
echo WshShell.Run "%~dp0start_Nova.bat", 0
echo Set WshShell = Nothing
) > run_silent.vbs

REM ---------------- STEP 6 ----------------
echo [6/6] Adding to Windows Startup...

set "STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

(
echo Set WshShell = CreateObject("WScript.Shell")
echo Set link = WshShell.CreateShortcut("%STARTUP%\NovaAssistant.lnk")
echo link.TargetPath = "%~dp0run_silent.vbs"
echo link.WorkingDirectory = "%~dp0"
echo link.Save
) > make_shortcut.vbs

cscript //nologo make_shortcut.vbs
del make_shortcut.vbs

echo =====================================
echo SETUP COMPLETE
echo =====================================
echo 1. Open .env and add TELEGRAM_TOKEN
echo 2. Reboot or run: run_silent.vbs
echo =====================================

pause
