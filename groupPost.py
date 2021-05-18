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


def driver():
    global driver
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://facebook.com")


def chrome_options():
    global chrome_options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--profile-directory=Default')
    # chrome_options.add_argument("--user-data-dir=chrome-data")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])


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
    sleepTime = 4
    implicitlyWaitTime = 20
    for i in range(2):
        driver.implicitly_wait(implicitlyWaitTime)
        actions.send_keys(Keys.BACK_SPACE)
        actions.send_keys(Keys.TAB * 4)
        time.sleep(sleepTime)
        actions.perform()
        print("Firast 10 tabs Working")

    actions.send_keys(Keys.TAB * 3)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Navigate Post area Successfully ")


    """ Nicer Approach
    # try:
    #     sleepTime = 4
    #     implicitlyWaitTime = 20
    #     for i in range(2):
    #         driver.implicitly_wait(implicitlyWaitTime)
    #         actions.send_keys(Keys.BACK_SPACE)
    #         actions.send_keys(Keys.TAB * 4)
    #         time.sleep(sleepTime)
    #         actions.perform()
    #         print("Firast 10 tabs Working")
    # 
    #     actions.send_keys(Keys.TAB * 3)
    #     actions.send_keys(Keys.ENTER)
    #     actions.perform()
    #     print("Navigate Post area Successfully ")
    # except:
    #     print("navigatePagePostAria function is not Working")
    #     print("Going For x Path")
    #     try:
    #         editButtonXpath = "//div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[1]"
    # 
    #         driver.find_element_by_xpath(editButtonXpath).click()
    #         print("X Path Workin in 'navigatePagePostAria' function")
    # 
    #     except:
    #         print("X path aslo not working in 'navigatePagePostAria' function")

     Nicer Approach End"""



def navigateEditButton():
    # driver.find_element_by_xpath("//div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div/div[1]").click()
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys(Keys.DOWN * 2)
    actions.perform()
    print("Navigate Edit Button area Successfully ")


def activePostAreaAndPostInPage():
    #driver.find_element_by_xpath("//div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div").click()
    sleepTime = 4
    implicitlyWaitTime = 20
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


chrome_options()
driver()
login()
driver.get("https://www.facebook.com/groups/402353916617590/permalink/1630582000461436/")
navigatePagePostAria()
# navigateEditButton()
# activePostAreaAndPostInPage()
