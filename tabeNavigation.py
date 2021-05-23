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

# the loop Running
def navigation():
    sleep_time = .25
    implicitly_wait_time = 2
    google_search_actions = ActionChains(driver)
    time.sleep(sleep_time)
    driver.get("https://google.com")
    google_search_actions.send_keys(random_google_search)

    total_tab = 3
    driver.implicitly_wait(implicitly_wait_time)
    time.sleep(sleep_time)
    for i in range(total_tab):
        google_search_actions.send_keys(Keys.TAB)
        print("Pressing * " + str(i + 1) + " * No Tab")
    google_search_actions.send_keys(Keys.ENTER)
    google_search_actions.perform()

for i in range(10):
    navigation()
    # actions.reset_actions()
    print("Pressing * " + str(i + 1) + " * st navigation function")
