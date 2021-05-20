#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib


def driver():
    global driver
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)


def chrome_options():
    global chrome_options
    chrome_options = Options()
    scriptDirectory = pathlib.Path().absolute()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--user-data-dir=chrome-data")
    chrome_options.add_argument('--profile-directory=Default')
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("user-data-dir=chrome-data")
    chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")


def actions():
    global actions
    actions = ActionChains(driver)


def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('my_facebook_username')
        password = os.environ.get('my_facebook_password')

        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


def navigatePagePostAria():
    total_tab = 23
    sleepTime = .25
    implicitlyWaitTime = 20

    for i in range(total_tab):
        driver.implicitly_wait(implicitlyWaitTime)
        actions.send_keys(Keys.BACK_SPACE)
        actions.send_keys(Keys.TAB)
        time.sleep(sleepTime)
        print("Pressing * " + str(i) + " * No Tab")
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Navigate Post area Successfully ")


def navigateEditPostButton():
    try:
        print("Using x path to click edit button ")
        #TODO: find x path and click edit button

        print("Navigate Edit Button Successfully ")
    except:
        print("When x path is not working function using ActionChains Keys.DOWN ")
        try:
            #TODO: Write loop like navigatePagePostAria() to find edit button
            print("Switch active aria successful")

            print("Navigate Edit Button Successfully ")
        except:
            print("in the navigateEditPostButton() function also not working")


def activePostAreaAndPostInPage():
    print("Writing Post in the post area Successfully ")


chrome_options()
driver()
driver.get("https://facebook.com")
actions()
login()
driver.get("https://www.facebook.com/groups/402353916617590/permalink/1630582000461436/")
navigatePagePostAria()
navigateEditPostButton()
activePostAreaAndPostInPage()

# driver.close()
