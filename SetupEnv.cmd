@echo off

REM Preventing Python from writing .pyc files
SET PYTHONDONTWRITEBYTECODE=1

echo "Check if Python is installed"
call python --version

if errorlevel 1 (
    echo "Python Not installed or not part of PATH"
    goto :ErrorSet
)

echo "Check if PIP is installed"
call pip --version
if errorlevel 1 (
    echo "Python Package Manager is not installed or not part of PATH"
    goto :ErrorSet
)

echo "Installing Python Virtual Env"
call pip install virtualenv

echo "Creating a Python virtual enviornment"
call virtualenv env

echo "Activate Python virtual enviornment"
call env\\Scripts\\activate

echo "Pip install - requirements.txt"
call pip install -r requirements.txt

goto :Finished

:ErrorSet
rem set errorlevel to current errorlevel
exit /B %errorlevel%
goto :EOF

:Finished
rem set errorlevel to SUCCESS i.e. 0
echo "Enviornment setup sucessful"
exit /B 0

goto :EOF