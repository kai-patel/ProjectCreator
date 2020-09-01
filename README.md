# ProjectCreator

## Introduction
The ProjectCreator script takes three command-line arguments, specifying the name of the project, and the email and password to login to your github account:
```
project.bat <project-name> <github-email> <github-password>
```

The project folder is set up to work with git, by generating a .git folder and a template README file. An initial commit is then registered with the message "Initial commit", and the script logs in to your GitHub account. A new repository is created on GitHub and the local repository is pushed to the new origin.

## Usage
```
project.bat <project-name> <github-email> <github-password>
```

To link the script to your account, please update the project.bat file with your config (lines 1 and 9),

```
cd <your-projects-folder>
git remote add origin "<your-account-link>/%1.git"
```

where \<your-account-link\>" looks like "https://github.com/your-account", and \<your-projects-folder\> is a Windows-style path to a directory.
