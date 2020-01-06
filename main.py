#!/usr/bin/env python3

""" Main file for ProjectCreator: an application to create and initialize new git projects """

__author__ = "Kai Patel"
__email__ = "00kaipatel@gmail.com"

import os
import sys

def initGit():
    print("[*] Initializing git")
    os.system(f"echo '# {project_name}' > README.md")
    os.system("git init && git add .")
    os.system("git commit -m \"initial commit\"")
    print("Project successfully created!")

def createProject():
    print("[*] Creating project folder")
    os.chdir("C:/Users/patel/OneDrive/Development/myProjects")
    if(os.system(f"mkdir {project_name}") == 0):
        print("[*] Changing into project directory")
        os.chdir(f"{project_name}")
        initGit()
        return True
    else:
        print("Could not create project folder!")
        sys.exit(1)

if __name__ == '__main__':
    project_name = str(sys.argv[1])
    if(createProject()):
        sys.exit(0)
    else:
        print("Could not create project, as a repository with the same name already exists!")
        sys.exit(1)