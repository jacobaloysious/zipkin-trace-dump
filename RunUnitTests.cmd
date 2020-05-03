@echo off

echo "Activate Python virtual enviornment"
call env\\Scripts\\activate.bat

echo "Run Nose Tests"
call nosetests -v

echo "Run Nose Tests with coverage - html output under cover dir"
call nosetests -v --with-coverage --cover-erase --cover-package=src --cover-html --cover-inclusive

echo "Remove all .PYC files"
cd src
del /S *.pyc
cd ..

goto :Finished

:ErrorSet
rem set errorlevel to current errorlevel
exit /B %errorlevel%
goto :EOF

:Finished
rem set errorlevel to SUCCESS i.e. 0
exit /B 0

goto :EOF
