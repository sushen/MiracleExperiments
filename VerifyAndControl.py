import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random


# Setting the chrome_options
global chrome_options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--profile-directory=Default')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

google_search = [
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

random_google_search = random.choice(google_search)

# Setting the Chrome Driver
global driver
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

# Setting the Actions
global actions
actions = ActionChains(driver)

search_field_xpath = "//input[@title='Search']"
print(search_field_xpath)
# 1st time Running

driver.get("https://google.com")


titleOfThePage = driver.title
print(titleOfThePage)

if titleOfThePage == "Google":
    actions.send_keys(random_google_search)

    total_tab = 3

    for i in range(total_tab):
        actions.send_keys(Keys.TAB)
        print("Pressing * " + str(i + 1) + " * No Tab")

    actions.send_keys(Keys.ENTER)
    actions.perform()
else:
    print("This page title is not Google ")

# # 2 second time Running
#
# time.sleep(5)
# actions.reset_actions()
#
# driver.get("https://google.com")
#
# actions.send_keys(random_google_search)
#
# total_tab = 3
# sleep_time = 1
# implicitly_wait_time = 4
#
# actions.reset_actions()
# driver.implicitly_wait(implicitly_wait_time)
# time.sleep(sleep_time)
#
# for i in range(total_tab):
#     actions.send_keys(Keys.TAB)
#     print("Pressing * " + str(i + 1) + " * No Tab")
#
# actions.send_keys(Keys.ENTER)
# actions.perform()
#
# # 3 second time Running
# time.sleep(5)
# actions.reset_actions()
#
# driver.get("https://google.com")
#
# actions.send_keys(random_google_search)
#
# total_tab = 3
# sleep_time = 1
# implicitly_wait_time = 4
#
# actions.reset_actions()
# driver.implicitly_wait(implicitly_wait_time)
# time.sleep(sleep_time)
#
# for i in range(total_tab):
#     actions.send_keys(Keys.TAB)
#     print("Pressing * " + str(i + 1) + " * No Tab")
#
# actions.send_keys(Keys.ENTER)
# actions.perform()


# # 4 time the loop Running
# def navigation():
#     time.sleep(5)
#     # actions.reset_actions()
#
#     driver.get("https://google.com")
#
#     actions.send_keys(random_google_search)
#
#     total_tab = 3
#     sleep_time = 1
#     implicitly_wait_time = 4
#
#
#     driver.implicitly_wait(implicitly_wait_time)
#     time.sleep(sleep_time)
#
#     for i in range(total_tab):
#         actions.send_keys(Keys.TAB)
#         print("Pressing * " + str(i + 1) + " * No Tab")
#
#     actions.send_keys(Keys.ENTER)
#     actions.perform()
#
#
# for i in range(10):
#     navigation()
#     actions.reset_actions()
#     print("Pressing * " + str(i + 1) + " * st navigation function")
