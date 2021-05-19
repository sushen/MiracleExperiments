#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8
#
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import pathlib


def options():
    global options
    options = Options()
    scriptDirectory = pathlib.Path().absolute()
    options.add_argument("--start-maximized")
    options.add_argument("--user-data-dir=chrome-data")
    options.add_argument('--profile-directory=Default')
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('disable-infobars')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("user-data-dir=chrome-data")
    options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")


def driver():
    global driver
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    # driver.get("https://facebook.com")

def actions():
    global actions
    actions = ActionChains(driver)


def login():
    driver.get("https://facebook.com")
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
        print("Selenium Calling Data From userdata folder bypass login ")
        pass


def navigatePagePostAria():
    sleepTime = 2
    implicitlyWaitTime = 30
    total_Tab = 23

    driver.get("https://www.facebook.com/groups/402353916617590/permalink/1630582000461436/")
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    print("2 second sleep and 30 sec implicit wait. ")

    actions.send_keys(Keys.TAB * total_Tab)
    print("I am pressing tab " + str(total_Tab) + " times")

    # for i in range(total_Tab):
    #     driver.implicitly_wait(implicitlyWaitTime)
    #     actions.send_keys(Keys.BACK_SPACE)
    #     # actions.send_keys(Keys.TAB)
    #     print("Now *" + str(i) + "* no tabs pressing")
    #
    # # actions.send_keys(Keys.ENTER)
    # time.sleep(sleepTime)
    # # actions.perform()


# def navigatePagePostAria():
#     try:
#         sleepTime = 0.5
#         implicitlyWaitTime = 20
#         total_Tab = 23
#         for i in range(total_Tab):
#             driver.implicitly_wait(implicitlyWaitTime)
#             actions.send_keys(Keys.BACK_SPACE)
#             actions.send_keys(Keys.TAB)
#             print("Now" + str(i) + "no tabs pressing")
#         actions.send_keys(Keys.ENTER)
#         time.sleep(sleepTime)
#         actions.perform()
#         print("Selenium ActionChains 'Keys.TAB'  working")
#     except:
#         print("Selenium ActionChains 'Keys.TAB' isn't working, Trying 'pyautogui.press('tab') commend' ")
#         try:
#             print("'pyautogui.press('tab') commend' is mute now")
#             # sleepTime = 4
#             # implicitlyWaitTime = 20
#             #
#             # for i in range(23):
#             #     time.sleep(sleepTime)
#             #     driver.implicitly_wait(implicitlyWaitTime)
#             #     pyautogui.press('tab')
#             #
#             # pyautogui.press('enter')
#         except:
#             print("'pyautogui.press('tab') commend' is also not working")


def navigateEditButton():
    sleepTime = 4
    implicitlyWaitTime = 30
    time.sleep(sleepTime)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys(Keys.DOWN * 2)
    # actions.send_keys(Keys.ENTER)
    time.sleep(sleepTime)
    actions.perform()
    print("Navigate Edit Button area Successfully ")


def activePostAreaAndPostInPage():
    #driver.find_element_by_xpath("//div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div").click()
    sleepTime = 4
    implicitlyWaitTime = 30
    #
    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    #
    active_post_area.send_keys(Keys.BACK_SPACE*5)
    #
    # active_post_area.send_keys(Keys.CONTROL, 'a')
    # active_post_area.send_keys(Keys.CONTROL, 'a')
    #
    # actions.send_keys("'driver.switch_to.active_element' "
    #                   "this code is a one of important snippet for facebook automation.")
    # time.sleep(sleepTime)
    #
    # print("Writing Post in the post area Successfully ")

    # for i in range(2):
    #     driver.implicitly_wait(implicitlyWaitTime)
    #     actions.send_keys(Keys.TAB * 2)
    #     print(str(i) + " tabs Working")

    # actions.send_keys(Keys.ENTER)
    actions.perform()


options()
driver()
login()
navigatePagePostAria()
# navigateEditButton()
# activePostAreaAndPostInPage()

driver.close()
