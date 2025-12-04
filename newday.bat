@echo off
setlocal EnableDelayedExpansion
cls

REM --- Détection de Python ---
set PY_VER=Not installed

python --version >nul 2>&1
if %ERRORLEVEL%==0 (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do (
        set PY_VER=%%i
    )
)

REM --- Menu ---
echo This util is meant to initialize a new working directory.
echo What programming language will you use ?
echo.
echo     1- Python [!PY_VER!]
echo.

set /p prog_choice="> "

if "!prog_choice!"=="1" (
    if "!PY_VER!"=="Not installed" (
        echo.
        echo Python n'est pas installe. Fin du programme.
        pause
        exit /b
    )

    echo.
    python utils/python/main.py
    echo.
    pause
    exit /b
)

echo.
echo Choix non gere. Fin du programme.
pause
exit /b
