import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# Time Counting
StartTime = time.time()
print("This Script Start " + time.ctime())

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

        driver.find_element_by_id("email").send_keys(username)
        driver.find_element_by_id("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


driver.get("https://www.facebook.com/messages/")
driver.implicitly_wait(20)
time.sleep(5)


def chatWindow():
    driver.implicitly_wait(10)
    time.sleep(2)
    chatWindowXpath = "//input[@placeholder='Search Messenger']"
    chatWindowPathAria = driver.find_elements_by_xpath(chatWindowXpath)

    if driver.find_elements_by_xpath(chatWindowXpath):
        chatWindowPathAria[0].click()
        chatWindowPathAria[0].send_keys(Keys.ENTER)
        chatWindowPathAria[0].send_keys(Keys.TAB)
        print(chatWindowXpath + "is the 1st Xpath and its working")
    else:
        print("Path Not Found and Copy New X path and Replace Old One")


def nextChatWindow():
    driver.implicitly_wait(10)
    time.sleep(2)
    print("Arrow Down Star")
    actionsForNext = ActionChains(driver)
    keyDown = actionsForNext.send_keys(Keys.DOWN)
    actionsForNext.send_keys(Keys.ENTER)
    actionsForNext.perform()
    print("Arrow Down End")


def fbMassageBoxArea():
    driver.implicitly_wait(10)
    time.sleep(2)
    fbMassageBoxXpath = "//div[@class='_1mf _1mj']"
    fbMassageBoxpathAria = driver.find_elements_by_xpath(fbMassageBoxXpath)

    if driver.find_elements_by_xpath(fbMassageBoxXpath):
        fbMassageBoxpathAria[0].click()
        print(fbMassageBoxXpath + "is the 1st Xpath and its working")
    else:
        print("Path Not Found and Copy New X path and Replace Old One")


def fbMassageForNewMassage():
    driver.implicitly_wait(10)
    time.sleep(2)
    activeActions = ActionChains(driver)
    activeActions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
    activeActions.send_keys("Hi")
    activeActions.send_keys(Keys.ENTER)
    activeActions.perform()


login()
chatWindow()
fbMassageBoxArea()
fbMassageForNewMassage()

for keyMove in range(15):
    time.sleep(5)
    chatWindow()

    # This is the function for doing something and incremental way
    actionsForNext = ActionChains(driver)
    keyMove = keyMove + 1
    actionsForNext.send_keys(Keys.DOWN * keyMove)
    actionsForNext.send_keys(Keys.ENTER)
    actionsForNext.perform()

    fbMassageBoxArea()
    fbMassageForNewMassage()



# Time Counting
EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
