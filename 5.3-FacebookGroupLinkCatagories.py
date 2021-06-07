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


def categoriesGroup():
    with open('categoriesGroup.txt') as file:
        lines = file.readlines()

        groupLinkList = []
        for groupLists in lines:
            groupLinkList.append(groupLists)
            groupIndex = (len(groupLinkList) - 1)
            print("Line Number : " + str(groupIndex))
            print("This line will be deleted :" + lines[groupIndex])
            del lines[groupIndex]
            deletedLink = lines[groupIndex]
            driver.get(deletedLink)
            line_index = 3
            deleteLines = None
            with open('groupCategorized.txt', 'r') as file_handler:
                deleteLines = file_handler.readlines()
            deleteLines.insert(line_index, deletedLink)
            with open('groupCategorized.txt', 'w') as file_handler:
                file_handler.writelines(deleteLines)
            print(input("Press any Key: "))


login()
categoriesGroup()
# print(input("Press any Key: "))



# Time Counting
EndTime = time.time()
print("This Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
