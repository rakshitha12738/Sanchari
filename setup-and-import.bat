@echo off
echo ===============================================
echo SANCHARI - MongoDB Setup and Import
echo ===============================================
echo.

REM Try to start MongoDB service
echo Checking MongoDB service...
sc query MongoDB | find "RUNNING" >nul
if %errorlevel% equ 0 (
    echo ✅ MongoDB service is already running
) else (
    echo Starting MongoDB service...
    net start MongoDB 2>nul
    if %errorlevel% equ 0 (
        echo ✅ MongoDB service started
    ) else (
        echo ⚠️  Could not start MongoDB service
        echo Please start MongoDB manually or run as Administrator
        echo.
        echo To install MongoDB:
        echo 1. Download from: https://www.mongodb.com/try/download/community
        echo 2. Install with default settings
        echo 3. Run this script again
        pause
        exit /b 1
    )
)

echo.
echo Waiting 3 seconds for MongoDB to be ready...
timeout /t 3 /nobreak >nul

echo.
echo Importing data into MongoDB...
node import-to-mongodb.js

if %errorlevel% equ 0 (
    echo.
    echo ===============================================
    echo ✅ Setup Complete!
    echo ===============================================
    echo.
    echo You can now start the server with:
    echo   npm start
    echo.
) else (
    echo.
    echo ===============================================
    echo ❌ Import Failed
    echo ===============================================
    echo.
    echo Please check if:
    echo 1. MongoDB is installed and running
    echo 2. Port 27017 is not blocked by firewall
    echo.
)

pause

