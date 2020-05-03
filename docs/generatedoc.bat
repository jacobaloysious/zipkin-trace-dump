REM Generate .rst files from source
call sphinx-apidoc -f -o _source/ ../src/

REM Generate htm
echo Executing make html
call make html
