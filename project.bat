cd C:\Users\patel\OneDrive\Development\myProjects
if "%~1" == "" GOTO end
mkdir %1
cd %1
echo "# %1" > README.md
git init && git add .
git commit -m "Initial commit"
python C:\Users\patel\OneDrive\Development\myProjects\ProjectCreator\main.py %1 %2
git remote add origin "https://github.com/kai-patel/%1.git"
git branch -M master
git push -u origin master
exit 0

end:
exit 1