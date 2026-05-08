@echo off
title 🛑 Stopping Nova...
color 0C

echo.
echo    [!] Killing all Nova processes...
echo.

:: Kill Python (The Brain)
taskkill /F /IM python.exe /T 2>nul
taskkill /F /IM pythonw.exe /T 2>nul

:: Kill Native Host if stuck (optional, usually managed by Firefox)
:: But good cleanup mechanism

echo.
echo    [✓] Nova has been stopped.
echo    [i] To restart, double-click 'start_nova.bat'
echo.
pause
