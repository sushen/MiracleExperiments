#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8
import pyautogui
from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Default')
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
actions = ActionChains(driver)


driver.get("https://facebook.com")

try:
    # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys("MangoPeople@021")
    driver.find_element_by_name("login").click()

except:
    pass

print(input("Press any Key: "))


driver.get("https://www.facebook.com/groups/402353916617590/permalink/1630582000461436/")

actions.send_keys(Keys.TAB * 23)
print(input("Press any Key: "))
driver.implicitly_wait(5)
actions.send_keys(Keys.ENTER)
actions.perform()

# pyautogui.press("down")
actions.send_keys(Keys.BACK_SPACE)
actions.send_keys(Keys.ARROW_DOWN)
print(input("Press any Key: "))
driver.implicitly_wait(5)
# actions.send_keys(Keys.ENTER)
actions.perform()

# driver.quit()