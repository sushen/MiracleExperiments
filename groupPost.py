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
        edit_post_button = driver.find_element_by_xpath("//span[normalize-space()='Edit post']")
        active_post_area = driver.switch_to.active_element
        active_post_area.click(edit_post_button)
        print("Using x path to click edit button ")
    except:
        print("Using path is not working using ActionChains Keys.DOWN ")
        try:
            keys_down = 4
            sleepTime = 1
            implicitlyWaitTime = 20

            active_post_area = driver.switch_to.active_element
            driver.implicitly_wait(implicitlyWaitTime)
            active_post_area.send_keys(Keys.DOWN)
            print("Switch active aria successful")

            for i in range(keys_down):
                actions.send_keys(Keys.DOWN)
                time.sleep(sleepTime)
                # actions.perform()
                print("Pressing * " + str(i) + " * No Down Key")
            # active_post_area.send_keys(Keys.ENTER)
            actions.perform()
            print("Navigate Edit Button Successfully ")
        except:
            print("in the navigateEditPostButton() area Keys.DOWN also not working")


def activePostAreaAndPostInPage():
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys("'driver.switch_to.active_element' "
                               "this code is a one of important snippet for facebook automation.")

    actions.perform()
    print("Writing Post in the post area Successfully ")

    for i in range(2):
        driver.implicitly_wait(implicitlyWaitTime)
        actions.send_keys(Keys.TAB * 5)
        print(str(i) + " tabs Working")
    actions.send_keys(Keys.ENTER)
    actions.perform()


chrome_options()
driver()
driver.get("https://facebook.com")
actions()
login()
driver.get("https://www.facebook.com/groups/402353916617590/permalink/1630582000461436/")
navigatePagePostAria()
navigateEditPostButton()

# driver.close()
