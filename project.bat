cd <your-projects-folder>
if "%~1" == "" GOTO end
mkdir %1
cd %1
(echo # %1) > README.md
git init && git add .
git commit -m "Initial commit"
python %~dp0\main.py %1 %2 %3
git remote add origin "<your-account-link>/%1.git"
git branch -M master
git push -u origin master
exit 0

end:
exit 1