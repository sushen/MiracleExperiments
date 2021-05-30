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
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

# Setting the driver
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


def navigateGroupPostAria():
    print("First Step Working")
    grpupPostEditBtnXpath = "//div[@aria-label='Actions for this post']"
    grpupPostXpathEditAria = driver.find_elements_by_xpath(grpupPostEditBtnXpath)
    if driver.find_elements_by_xpath(grpupPostEditBtnXpath):
        grpupPostXpathEditAria[0].click()
        print(grpupPostXpathEditAria)
    else:
        print("Path Not Found")

def navigateGroupPostEditBtnSecondndStep():
    navigateGroupPostAriaActions = ActionChains(driver)
    total_tab = 1
    for i in range(total_tab):
        navigateGroupPostAriaActions.send_keys(Keys.DOWN)
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

    total_tab = 7
    for i in range(total_tab):
        driver.implicitly_wait(implicitlyWaitTime)
        activePostAreaAndPostInPageActions.send_keys(Keys.TAB)
        print(str(i + 1) + " tabs Working for saving edited post")
    activePostAreaAndPostInPageActions.send_keys(Keys.ENTER)
    activePostAreaAndPostInPageActions.perform()


login()

groupLinkLists = ["https://www.facebook.com/groups/132593590202911/permalink/3800069366788630/",
                  "https://www.facebook.com/groups/601242797290982/permalink/997721077643150/",
                  "https://www.facebook.com/groups/729769827368286/permalink/1466696920342236/"
                  ]


def groupPost():
    index = 0

    for groupLinkList in groupLinkLists:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(groupLinkList)

        print("We are in " + str(index) + " No " + groupLinkList + " Group")
        index += 1

        navigateGroupPostAria()
        time.sleep(5)

        navigateGroupPostEditBtnSecondndStep()
        time.sleep(5)

        activeGroupAreaAndPostInGroup()
        time.sleep(5)

        print(input("Press any Key: "))


groupPost()
