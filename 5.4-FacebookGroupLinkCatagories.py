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
import collections

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

# Setting the driver
global driver
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver.get("https://facebook.com")


def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('facebook_zrliqi_email')
        password = os.environ.get('facebook_zrliqi_pass')
        print("Facebook Username :" + username)
        # print(password)
        # print(input("Press any Key: "))

        driver.find_element_by_id("email").send_keys(username)
        driver.find_element_by_id("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


def findAndRemoveDuplicate():
    with open('categoriesGroup.txt', 'r') as file:
        groupLinks = file.readlines()
        groupLinkSet = set(groupLinks)
        # This loop Expression detect all duplicate item inside list
        duplicateLinks = [item for item, count in collections.Counter(groupLinks).items() if count > 1]
        duplicateLinkSet = set(duplicateLinks)
        uniqueFile = groupLinkSet - duplicateLinkSet
        with open('groupCategorized.txt', 'r') as file:
            sortedGroupLinks = file.readlines()
            sortedGroupLinksSet = set(sortedGroupLinks)
        with open('categoriesGroup.txt', 'w') as file:
            # this line delete 2 set String which I store in variable
            sortedUniqueFile = groupLinkSet - sortedGroupLinksSet
            file.writelines(sortedUniqueFile)
        print("We work " + str(len(sortedGroupLinks))
              + " links and \nOur Total group Link is "
              + str(len(sortedGroupLinks)
                    + (len(groupLinks))))


def copyCurrentUrl():
    pc.copy(driver.current_url)
    groupUrl = pc.paste()
    print("This line will be deleted :" + groupUrl)


def switchWindow():
    currentWindow = driver.current_window_handle
    print("Current Group Window :" + currentWindow)
    window_before = driver.window_handles[0]
    print("This is index of Current Window :" + window_before)

    driver.execute_script("window.open('');")
    window_after = driver.window_handles[1]
    print("New Window Index :" + window_after)
    driver.switch_to.window(window_after)
    driver.get("https://docs.google.com/spreadsheets/d/1V9jCslR-OpBoa5l8xDs2VkCASx8FdrJqLWOUPHmWcY8/")
    driver.switch_to.window(window_before)
    time.sleep(5)
    driver.switch_to.window(window_after)
    driver.close()
    driver.switch_to.window(window_before)

def categoriesGroup():
    with open('categoriesGroup.txt') as file:
        lines = file.readlines()
        print("We have to work with " + str(len(lines)) + " link")

        groupLinkList = []
        for groupLists in lines:
            groupLinkList.append(groupLists)
            groupIndex = (len(groupLinkList) - 1)
            print("Line Number : " + str(groupIndex))

            deletedLink = lines[groupIndex]
            driver.get(deletedLink)

            copyCurrentUrl()
            print(input("Press any Key: "))

            line_index = 3
            deleteLines = None
            with open('groupCategorized.txt', 'r') as file_handler:
                deleteLines = file_handler.readlines()
            deleteLines.insert(line_index, deletedLink)
            with open('groupCategorized.txt', 'w') as file_handler:
                file_handler.writelines(deleteLines)


login()
findAndRemoveDuplicate()
categoriesGroup()
# print(input("Press any Key: "))


# Time Counting
EndTime = time.time()
print("This Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
