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

group_post = [
    "Hello, \nI am very excited about Python and Automation.\nI like to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\nContact me personally.\nI will be glad to help you personally.",
    "Hi, \nI am very excited about Automation and Python.\nI like to help 2 people learning Automation \nand Python in this week.\nIf you 1 hours time in the evening after 6 p.m\npersonally contact me.\nI will be glad to help you one to one session.",
    "Greeting, \nI am very excited about Python and Automation.\nI want to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\nContact me personally.\nI will be glad to help you personally.",
    "Hi Python Lover, \nI am very excited about Python and Automation.\nI like to help 2 people learning Python\nand Automation in this week.\nIf you 1 hours time in the evening after 6 p.m\npersonally contact me.\nI will be glad to help you one to one session."

]
# Setting the driver
global driver
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver.get("https://facebook.com")

def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('facebook_zrliqi_email')
        password = os.environ.get('facebook_zrliqi_pass')

        driver.find_element("email").send_keys(username)
        driver.find_element("pass").send_keys(password)
        driver.find_element("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


def navigateGroupPostBtn():
    grpupPostXpath = "//span[contains(text(),'s on your mind,')]"
    grpupPostX2ndpath = "//span[contains(text(),'Create a public post…')]"

    grpupPostXpathAria = driver.find_elements_by_xpath(grpupPostXpath)
    grpupPost2ndXpathAria = driver.find_elements_by_xpath(grpupPostX2ndpath)

    if driver.find_elements_by_xpath(grpupPostXpath):
        grpupPostXpathAria[0].click()
        print(grpupPostXpath + "is the 1st Xpath and its working")

    elif driver.find_elements_by_xpath(grpupPostX2ndpath):
        grpupPost2ndXpathAria[0].click()
        print(grpupPostX2ndpath + "is the 2nd Xpath and its working")

    else:
        print("Path Not Found")


def activeGroupAreaAndPostInGroup():
    random_profile_post = random.choice(group_post)
    sleepTime = .5
    implicitlyWaitTime = 20

    activePostAreaAndPostInPageActions = ActionChains(driver)
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    activePostAreaAndPostInPageActions.send_keys(random_profile_post)

    activePostAreaAndPostInPageActions.perform()
    print("Writing Post in the post area Successfully ")
    # activePostAreaAndPostInPageActions.reset_actions()


def activeGroupAreaPostBtn():
    PostBtnXpath = "// span[contains(text(), 'Post')]"
    grpupPostBtn = driver.find_elements_by_xpath(PostBtnXpath)
    if driver.find_elements_by_xpath(PostBtnXpath):
        grpupPostBtn[0].click()
        print(grpupPostBtn)
    else:
        print("Post Button Not Found")


login()

testGroupLists = [
    "https://www.facebook.com/groups/3051881851503314/",
    "https://www.facebook.com/groups/10ms.programming/",
    "https://www.facebook.com/groups/601242797290982/",
    "https://www.facebook.com/groups/729769827368286/",
    "https://www.facebook.com/groups/2092683587684490/",
    "https://www.facebook.com/groups/132593590202911/"
]
groupLists = [
    "https://www.facebook.com/groups/pythonsnake2/",
    "https://www.facebook.com/groups/3051881851503314/",
    "https://www.facebook.com/groups/10ms.programming/",
    "https://www.facebook.com/groups/softwebtuts/",
    "https://www.facebook.com/groups/997975157020313/",
    "https://www.facebook.com/groups/stacklearner/",
    "https://www.facebook.com/groups/366190054572553/",
    "https://www.facebook.com/groups/pypcom/",
    "https://www.facebook.com/groups/118355661537061/",
    "https://www.facebook.com/groups/402353916617590/",
    "https://www.facebook.com/groups/pythonsnake/",
    "https://www.facebook.com/groups/youngcodersLP/",
    "https://www.facebook.com/groups/pythonQA/",
    "https://www.facebook.com/groups/pythonprogrammingclub/",
    "https://www.facebook.com/groups/python/",
    "https://www.facebook.com/groups/InsaneTech/",
    "https://www.facebook.com/groups/302806677466652/",
    "https://www.facebook.com/groups/python.morioh/",
    "https://www.facebook.com/groups/2030059543915989/",
    "https://www.facebook.com/groups/493854764823932/",
    "https://www.facebook.com/groups/828941034587334/",
    "https://www.facebook.com/groups/135196957162117/",
    "https://www.facebook.com/groups/mathfordatascience/",
    "https://www.facebook.com/groups/2616981278627207",
    "https://www.facebook.com/groups/djangodevelopersnetwork/",
    "https://www.facebook.com/groups/2834322033475732/",
    "https://www.facebook.com/groups/2059467967664033/",
    "https://www.facebook.com/groups/4423889427637168/",
    "https://www.facebook.com/groups/551975265238987/",
    "https://www.facebook.com/groups/341334433330410/",
    "https://www.facebook.com/groups/1955664064497065/",
    "https://www.facebook.com/groups/programmingbasicsconcepts/",
    "https://www.facebook.com/groups/1914592312155348",
    "https://www.facebook.com/groups/pirawenpython/",
    "https://www.facebook.com/groups/programming.school/",
    "https://www.facebook.com/groups/632595694006151/",
    "https://www.facebook.com/groups/142201439713193/",
    "https://www.facebook.com/groups/pythonprogrammingbeginners/",
    "https://www.facebook.com/groups/machine.learning.bangladesh/",
    "https://www.facebook.com/groups/pythonbd/"

]


def groupPost():
    index = 0

    for groupLinkList in testGroupLists:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(groupLinkList)

        print("We are in " + str(index) + " No " + groupLinkList + " Group")
        index += 1

        navigateGroupPostBtn()
        time.sleep(5)

        activeGroupAreaAndPostInGroup()
        time.sleep(5)

        activeGroupAreaPostBtn()
        time.sleep(10)
        print(input("Press any Key: "))


groupPost()
