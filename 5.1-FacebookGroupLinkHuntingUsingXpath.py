import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random
import pyperclip as pc


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


def fbGroupArea():
    driver.implicitly_wait(30)
    time.sleep(2)
    fbGroupAreaXpath = "//input[@placeholder='Search groups']"
    fbGroupAreaXpathAria = driver.find_elements_by_xpath(fbGroupAreaXpath)

    if driver.find_elements_by_xpath(fbGroupAreaXpath):
        fbGroupAreaXpathAria[0].click()
        print(fbGroupAreaXpath + "is the 1st Xpath and its working")
    else:
        print("Path Not Found ")


def firstGroupLink():
    driver.implicitly_wait(30)
    time.sleep(2)
    firstGroupActions = ActionChains(driver)
    total_tab = 5
    for i in range(total_tab):
        firstGroupActions.send_keys(Keys.TAB)
        print(str(i + 1) + " tabs Working.")
    firstGroupActions.send_keys(Keys.ENTER)
    firstGroupActions.perform()
    print("We are in first Group")


def groupOpenNewTab():
    driver.implicitly_wait(30)
    time.sleep(2)
    groupOpenActions = ActionChains(driver)
    groupOpenActions.send_keys(Keys.ENTER)
    groupOpenActions.perform()
    print("We are in New Tab")


def nextGroup():
    driver.implicitly_wait(30)
    time.sleep(2)
    nextGroupActions = ActionChains(driver)
    nextGroupActions.send_keys(Keys.TAB)
    nextGroupActions.send_keys(Keys.ENTER)
    nextGroupActions.perform()
    print("We are in New Tab")


login()
driver.get("https://www.facebook.com/groups/")
fbGroupArea()
firstGroupLink()

groupUrl = []
for i in range(50):
    driver.implicitly_wait(30)
    groupOpenNewTab()
    nextGroup()
    pc.copy(driver.current_url)
    groupUrl = pc.paste()
    print(groupUrl)

    # Write Url in a file
    groupUrlForList = groupUrl

    line_index = 3
    lines = None
    with open('file.txt', 'r') as file_handler:
        lines = file_handler.readlines()

    lines.insert(line_index, groupUrlForList)

    with open('file.txt', 'w') as file_handler:
        file_handler.writelines(lines)

    time.sleep(5)
    print("We are in " + str(i) + " No Group")
    # print(input("Press any Key: "))



# Time Counting
EndTime = time.time()
print("This Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
