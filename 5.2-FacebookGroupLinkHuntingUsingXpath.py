import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.window import WindowTypes
import pathlib
import random
import pyperclip as pc
import winsound

# Time Counting


StartTime = time.time()
print("This Script Start " + time.ctime())

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
        username = os.environ.get('my_facebook_username')
        password = os.environ.get('my_facebook_password')
        print(username)
        # print(password)
        # print(input("Press any Key: "))

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
    fbGroupAreaXpath = "//input[@placeholder='Search Groups']"
    fbGroupAreaXpathAria = driver.find_elements_by_xpath(fbGroupAreaXpath)

    if driver.find_elements_by_xpath(fbGroupAreaXpath):
        fbGroupAreaXpathAria[0].click()
        print(fbGroupAreaXpath + "is the 1st Xpath and its working")
    else:
        print("Path Not Found ")
        print(input("You Path is not found it will create wrong Navigation fixed it: "))


def firstGroupLink():
    driver.implicitly_wait(30)
    time.sleep(1)
    firstGroupActions = ActionChains(driver)
    total_tab = 9
    for i in range(total_tab):
        firstGroupActions.send_keys(Keys.TAB)
        print(str(i + 1) + " tabs Working.")
    firstGroupActions.send_keys(Keys.ENTER)
    firstGroupActions.perform()
    print("We are in first Group")


def nextGroup():
    driver.implicitly_wait(30)
    time.sleep(1)
    nextGroupActions = ActionChains(driver)
    nextGroupActions.send_keys(Keys.TAB)
    nextGroupActions.send_keys(Keys.ENTER)
    nextGroupActions.perform()
    print("We are in New Tab")


def bigScroll():
    driver.implicitly_wait(30)
    time.sleep(2)
    bigScrollActions = ActionChains(driver)
    bigScrollActions.send_keys(Keys.PAGE_DOWN)
    bigScrollActions.perform()
    print("We are in New Tab")


def smallScroll():
    driver.implicitly_wait(30)
    time.sleep(2)
    smallScrollActions = ActionChains(driver)
    smallScrollActions.send_keys(Keys.ARROW_DOWN*2)
    smallScrollActions.perform()
    print("We are in New Tab")


def groupOpenNewTab():
    driver.implicitly_wait(30)
    time.sleep(2)
    groupOpenActions = ActionChains(driver)
    groupOpenActions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL)
    groupOpenActions.perform()
    print("We are in New Tab")


def bigNextGroup():
    bigNextLoopStartTime = time.time()
    for i in range(835):
            driver.implicitly_wait(30)
            time.sleep(1)
            bigNextActions = ActionChains(driver)
            bigNextActions.send_keys(Keys.TAB)
            bigNextActions.send_keys(Keys.ARROW_DOWN*2)
            bigNextActions.perform()
            print("We are in " + str(i) + " no Tab")

    winsound.Beep(440, 1500)
    bigNextLoopEndTime = time.time()
    bigNextLoopTotalRunningTime = bigNextLoopEndTime - bigNextLoopStartTime
    print("This Script is running for " + str(int(bigNextLoopTotalRunningTime / 60)) + " Minutes.")


def switchBrowserTab():
    window_before = driver.window_handles[0]
    print("Group Window :" + window_before)

    window_after = driver.window_handles[1]
    print("Single Group Link Window :" + window_after)

    driver.switch_to.window(window_after)
    pc.copy(driver.current_url)
    groupUrl = pc.paste()
    print(driver.title)
    print(groupUrl)


    # Write Url in a file
    # groupUrlForList = str(i) + ". " + groupUrl + "\n"
    groupUrlForList = groupUrl + "\n"

    line_index = 3
    lines = None
    with open('file.txt', 'r') as file_handler:
        lines = file_handler.readlines()

    lines.insert(line_index, groupUrlForList)

    with open('file.txt', 'w') as file_handler:
        file_handler.writelines(lines)

    # driver.switch_to.window(window_before)

    time.sleep(5)
    driver.close()


def groupLinkCopy():
    loopStartTime = time.time()
    for i in range(50):
        currentWindow = driver.current_window_handle
        print("Current Window : " + currentWindow)

        driver.implicitly_wait(30)
        groupOpenNewTab()
        nextGroup()
        switchBrowserTab()

        driver.implicitly_wait(30)
        time.sleep(4)

        driver.switch_to.window(currentWindow)
        smallScroll()

        driver.implicitly_wait(30)
        time.sleep(4)
        print("We are in " + str(i) + " No Group")
        # print(input("Press any Key: "))

    loopEndTime = time.time()
    loopTotalRunningTime = loopEndTime - loopStartTime
    print("This Script is running for " + str(int(loopTotalRunningTime / 60)) + " Minutes.")


login()
driver.get("https://www.facebook.com/groups/")
driver.implicitly_wait(30)
time.sleep(4)
fbGroupArea()
driver.implicitly_wait(30)
time.sleep(4)
firstGroupLink()
# print(input("Press any Key: "))
bigNextGroup()
print(input("Press any Key: "))
# groupLinkCopy()

duration = 500  # milliseconds
freq = 440  # Hz
for i in range(10):
    driver.implicitly_wait(30)
    groupLinkCopy()
    winsound.Beep(freq, duration)
    # bigScroll()
    time.sleep(5)
    print(input(str(i) + "' st 22 Group Link Recorded Press any key to continue: "))



# Time Counting
EndTime = time.time()
print("This Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
