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


def driver():
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

def navigateGroupJoinBtn():
    navigateGroupJoinBtnActions = ActionChains(driver)
    total_tab = 19
    sleepTime = 1
    implicitlyWaitTime = 20

    time.sleep(sleepTime)
    for i in range(total_tab):
        driver.implicitly_wait(implicitlyWaitTime)
        navigateGroupJoinBtnActions.send_keys(Keys.TAB)
        print("Pressing * " + str(i + 1) + " * No Tab")
    navigateGroupJoinBtnActions.send_keys(Keys.ENTER)
    navigateGroupJoinBtnActions.perform()
    print("Navigate Groum Join Btn Successfully ")



driver()
login()

groupLists = [
    "https://www.facebook.com/groups/pythonsnake2/",
    "https://www.facebook.com/groups/pythonbd/",
    "https://www.facebook.com/groups/3051881851503314/",
    "https://www.facebook.com/groups/210517586045027/",
    "https://www.facebook.com/groups/10ms.programming/",
    "https://www.facebook.com/groups/softwebtuts/",
    "https://www.facebook.com/groups/493854764823932/",
    "https://www.facebook.com/groups/142201439713193/",
    "https://www.facebook.com/groups/997975157020313/",
    "https://www.facebook.com/groups/pythonprogrammingbeginners/",
    "https://www.facebook.com/groups/stacklearner/",
    "https://www.facebook.com/groups/366190054572553/",
    "https://www.facebook.com/groups/pypcom/",
    "https://www.facebook.com/groups/118355661537061/",
    "https://www.facebook.com/groups/402353916617590/",
    "https://www.facebook.com/groups/HTML.CSSandJavaScript/",
    "https://www.facebook.com/groups/pythonsnake/",
    "https://www.facebook.com/groups/308915099815447/",
    "https://www.facebook.com/groups/youngcodersLP/",
    "https://www.facebook.com/groups/pythonQA/",
    "https://www.facebook.com/groups/DeepNetGroup/",
    "https://www.facebook.com/groups/135196957162117/",
    "https://www.facebook.com/groups/pythonprogrammingclub/",
    "https://www.facebook.com/groups/2059467967664033/",
    "https://www.facebook.com/groups/4423889427637168/",
    "https://www.facebook.com/groups/programming.school/",
    "https://www.facebook.com/groups/python/",
    "https://www.facebook.com/groups/InsaneTech/",
    "https://www.facebook.com/groups/632595694006151/",
    "https://www.facebook.com/groups/bengaliprogramming/",
    "https://www.facebook.com/groups/302806677466652/",
    "https://www.facebook.com/groups/machine.learning.bangladesh/",
    "https://www.facebook.com/groups/pirawenpython/",
    "https://www.facebook.com/groups/programmingbasicsconcepts/",
    "https://www.facebook.com/groups/1914592312155348/",
    "https://www.facebook.com/groups/551975265238987/",
    "https://www.facebook.com/groups/2834322033475732/",
    "https://www.facebook.com/groups/python.morioh/",
    "https://www.facebook.com/groups/mathfordatascience/",
    "https://www.facebook.com/groups/1955664064497065/",
    "https://www.facebook.com/groups/2030059543915989/",
    "https://www.facebook.com/groups/djangodevelopersnetwork/",
    "https://www.facebook.com/groups/341334433330410/",
    "https://www.facebook.com/groups/699038760180241/",
    "https://www.facebook.com/groups/2616981278627207",
    "https://www.facebook.com/groups/828941034587334/"
]

for groupLinkList in groupLists:
    driver.get(groupLinkList)
    print(groupLinkList + " link")
    time.sleep(5)



