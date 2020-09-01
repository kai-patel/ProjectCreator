#!/usr/bin/env python3

""" Main file for ProjectCreator: an application to create and initialize new git projects """

__author__ = "Kai Patel"
__email__ = "00kaipatel@gmail.com"

import os
import sys
from selenium import webdriver

project_name = str(sys.argv[1])

user_ = "00kaipatel@gmail.com"
pass_ = str(sys.argv[2])

def main():
    driver = webdriver.Chrome()
    driver.get("http://www.github.com/login")

    #sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
    #sign_in.submit()

    username = driver.find_element_by_xpath("//*[@id='login_field']")
    username.send_keys(user_)

    password = driver.find_element_by_xpath("//*[@id='password']")
    password.send_keys(pass_)

    login_button = driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]")
    login_button.submit()

    driver.get("https://github.com/new")

    repo_name = driver.find_element_by_xpath("//*[@id='repository_name']")
    repo_name.send_keys(project_name)

    create_repo_button = driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
    create_repo_button.submit()
    return 0

if __name__ == "__main__":
    main()