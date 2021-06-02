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


driver.implicitly_wait(20)
time.sleep(5)

profileLinkLists = [
    # "https://www.facebook.com/rakeshkumar.lenka.71",
    "https://www.facebook.com/nihan.mahmud.39",
    "https://www.facebook.com/rizwan.ansari.1422409"
]


def personalProfileNav():
    index = 0
    for profileLinkList in profileLinkLists:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(profileLinkList)

        print("We are in " + str(index) + " No Profile link : " + profileLinkList)
        index += 1
        # print(input("Press any Key: "))

        # Navigate Profile Massage Aria
        ProfileMassageBtnXpath = "// span[contains(text(), 'Message')]"
        ProfileMassageBtnXpathAria = driver.find_elements_by_xpath(ProfileMassageBtnXpath)
        if driver.find_elements_by_xpath(ProfileMassageBtnXpath):
            ProfileMassageBtnXpathAria[0].click()
            print(ProfileMassageBtnXpathAria[0])
        elif driver.find_elements_by_xpath(ProfileMassageBtnXpath):
            ProfileMassageBtnXpathAria[1].click()
            print(ProfileMassageBtnXpathAria[1])
        else:
            print("Path Not Found")
        print(input("Press any Key: "))
        print("Profile Massage Aria")

        # Navigate Below Massage Aria
        massageBtnXpath = "//div[@class='_1mf _1mj']"
        massageBtnXpathAria = driver.find_elements_by_xpath(massageBtnXpath)
        if driver.find_elements_by_xpath(massageBtnXpath):
            massageBtnXpathAria[0].click()
            print(massageBtnXpathAria)
        else:
            print("Path Not Found")
        # print(input("Press any Key: "))
        print("Below Massage Aria")

        # Send Massage
        driver.implicitly_wait(10)
        time.sleep(2)
        activeActions = ActionChains(driver)
        activeActions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        activeActions.send_keys("Why we need automation in our regular life?")
        activeActions.send_keys(Keys.ENTER)
        activeActions.perform()
        print("Send Personal Massage")
        time.sleep(5)
        print(input("Press any Key: "))

        # Close Massage
        closeMassageBtnXpath = "//div[@aria-label='Close chat']//*[local-name()='svg']"
        closeMassageBtnXpathAria = driver.find_elements_by_xpath(closeMassageBtnXpath)
        if driver.find_elements_by_xpath(closeMassageBtnXpath):
            closeMassageBtnXpathAria[0].click()
            print(closeMassageBtnXpathAria)
        else:
            print("Path Not Found")
        print("Close Massage Aria")
        # print(input("Press any Key: "))


personalProfileNav()

# Time Counting
EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
