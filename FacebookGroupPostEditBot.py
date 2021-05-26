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

# Setting the chrome_options
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


def driver():
    global driver
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://facebook.com")


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

def navigateGroupPostAria():
    navigateGroupPostAriaActions = ActionChains(driver)
    total_tab = 40
    sleepTime = .25
    implicitlyWaitTime = 20

    for i in range(total_tab):
        driver.implicitly_wait(implicitlyWaitTime)
        # navigateGroupPostAriaActions.send_keys(Keys.BACK_SPACE)
        navigateGroupPostAriaActions.send_keys(Keys.TAB)
        time.sleep(sleepTime)
        print("Pressing * " + str(i) + " * No Tab")
    navigateGroupPostAriaActions.send_keys(Keys.ENTER)
    navigateGroupPostAriaActions.perform()
    print("Navigate Post area Successfully ")

def activeGroupAreaAndPostInGroup():
    sleepTime = .5
    implicitlyWaitTime = 20

    activePostAreaAndPostInPageActions = ActionChains(driver)
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    activePostAreaAndPostInPageActions.send_keys(random_profile_post)

    activePostAreaAndPostInPageActions.perform()
    print("Writing Post in the post area Successfully ")

    total_tab = 9
    for i in range(total_tab):
        driver.implicitly_wait(implicitlyWaitTime)
        activePostAreaAndPostInPageActions.send_keys(Keys.TAB)
        print(str(i + 1) + " tabs Working for saving edited post")
    activePostAreaAndPostInPageActions.send_keys(Keys.ENTER)
    activePostAreaAndPostInPageActions.perform()

driver()
login()

groupLinkLists = ["https://www.facebook.com/groups/601242797290982/",
                 "https://www.facebook.com/groups/2092683587684490//",
                 "https://www.facebook.com/groups/729769827368286/"
                 ]

for groupLinkList in groupLinkLists:
    driver.get(groupLinkList)
    print(groupLinkList + " link")
    print(input("Press any Key: "))

    time.sleep(5)
    navigateGroupPostAria()

    time.sleep(5)
    activeGroupAreaAndPostInGroup()
