import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# Setting the chrome_options
global chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")


def driver():
    global driver
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://facebook.com")


def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('facebook_zrliqi_email')
        password = os.environ.get('facebook_zrliqi_pass')

        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


def navigateGroupJoinBtn():

    print("Join Group")


driver()
login()


groupLists = [
    "https://www.facebook.com/groups/improgramer/",
    "https://www.facebook.com/groups/pythonbd/",
    "https://www.facebook.com/groups/HTML.CSSandJavaScript/",
    "https://www.facebook.com/groups/308915099815447/",
    "https://www.facebook.com/groups/DeepNetGroup/",
    "https://www.facebook.com/groups/bengaliprogramming/",
    "https://www.facebook.com/groups/699038760180241/"


]

for groupLinkList in groupLists:
    driver.get(groupLinkList)
    print(groupLinkList + " link")
    time.sleep(5)

    navigateGroupJoinBtn()
    time.sleep(10)
    print(input("Press any Key: "))
