import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

facebook_posts = [
    "1.Hello \nI am very excited about Python and Automation.\nI like to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\nContact me personally.\nI will be glad to help you personally.",
    "2.Hi \nI am very excited about Automation and Python.\nI like to help 2 people learning Automation \nand Python in this week.\nIf you 1 hours time in the evening after 6 p.m\npersonally contact me.\nI will be glad to help you one to one session.",
    "3.Greeting \nI am very excited about Python and Automation.\nI want to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\nContact me personally.\nI will be glad to help you personally.",
    "4.Hi Python Lover \nI am very excited about Python and Automation.\nI like to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\npersonally contact me.\nI will be glad to help you one to one session."

]

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
    sleepTime = 1
    implicitlyWaitTime = 20

    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    EditBtnSecondndStep = "//span[contains(text(),'Edit post')]"
    driver.find_element_by_xpath(EditBtnSecondndStep).click()



def activeGroupAreaAndPostInGroup():
    random_profile_post = random.choice(facebook_posts)

    sleepTime = 1
    implicitlyWaitTime = 20

    activePostAreaAndPostInPageActions = ActionChains(driver)
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)

    activePostAreaAndPostInPageActions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
    time.sleep(sleepTime)

    activePostAreaAndPostInPageActions.send_keys(random_profile_post)

    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    activePostAreaAndPostInPageActions.perform()
    print("Writing Post in the post area Successfully ")


def clickSaveBtn():
    sleepTime = 1
    implicitlyWaitTime = 20

    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)

    SaveBtnXpath = "//span[contains(text(),'Save')]"
    driver.find_element_by_xpath(SaveBtnXpath).click()



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

        clickSaveBtn()
        time.sleep(5)

        # print(input("Press any Key: "))


groupPost()
