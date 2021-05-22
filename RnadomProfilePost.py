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
import random

facebook_posts = [
    "1.' driver.switch_to.active_element' ",
    "2.this code is a one of important snippet for facebook automation.",
    "3.' driver.switch_to.active_element' ",
    "4.this code is a one of important snippet for facebook automation.",
    "5.' driver.switch_to.active_element' ",
    "6.this code is a one of important snippet for facebook automation.",
    "7.' driver.switch_to.active_element' ",
    "8.this code is a one of important snippet for facebook automation.",
    "9.' driver.switch_to.active_element' ",
    "10.this code is a one of important snippet for facebook automation.",
    "11.' driver.switch_to.active_element' ",
    "12.this code is a one of important snippet for facebook automation.",
    "13.' driver.switch_to.active_element' ",
    "14.this code is a one of important snippet for facebook automation.",
    "15.' driver.switch_to.active_element' ",
    "16.this code is a one of important snippet for facebook automation."

]

print(random.choice(facebook_posts))

random_profile_post = random.choice(facebook_posts)


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
    total_tab = 57
    sleep_time = .25
    implicitly_wait_time = 60

    for i in range(total_tab):
        driver.implicitly_wait(implicitly_wait_time)
        actions.send_keys(Keys.BACK_SPACE)
        actions.send_keys(Keys.TAB)
        time.sleep(sleep_time)
        print("Pressing * " + str(i) + " * No Tab")
    actions.send_keys(Keys.ENTER)
    actions.perform()
    # actions.reset_actions()

    print("Navigate Post area Successfully ")


def activePostAreaAndPostInPage():
    sleep_time = 1
    implicitly_wait_time = 10
    time.sleep(sleep_time)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitly_wait_time)
    time.sleep(sleep_time)
    active_post_area.send_keys(random_profile_post)

    # actions.perform()
    # actions.reset_actions()
    print("Writing* Post in the post area Successfully ")

    # for i in range(2):
    #     driver.implicitly_wait(implicitly_wait_time)
    #     actions.send_keys(Keys.TAB * 5)
    #     print(str(i) + " tabs Working")
    # actions.send_keys(Keys.ENTER)
    # actions.perform()


def navigatePostButton():
    total_tab = 10
    sleep_time = 1
    implicitly_wait_time = 4

    actions.reset_actions()
    driver.implicitly_wait(implicitly_wait_time)
    time.sleep(sleep_time)

    for i in range(total_tab):
        actions.send_keys(Keys.TAB)
        print("Pressing * " + str(i + 1) + " * No Tab")

    actions.send_keys(Keys.ENTER)
    actions.perform()


    print("navigate Post *Button area Successfully ")


chrome_options()
driver()
driver.get("https://facebook.com")
actions()
login()
driver.get("https://www.facebook.com/sushen.biswas/")
navigatePagePostAria()
activePostAreaAndPostInPage()
navigatePostButton()

# def randomPost():
#     total_post = 10
#     sleepTime = 4
#     implicitlyWaitTime = 30
#     time.sleep(sleepTime)
#     for i in range(total_post):
#         driver.get("https://www.facebook.com/sushen.biswas/")
#         driver.implicitly_wait(implicitlyWaitTime)
#         time.sleep(sleepTime)
#         navigatePagePostAria()
#         activePostAreaAndPostInPage()
#
# randomPost()
