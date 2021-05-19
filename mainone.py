import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui


def driver():
    global driver
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://facebook.com")


def chrome_options():
    global chrome_options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--profile-directory=Default')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

def actions():
    global actions
    actions = ActionChains(driver)

def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = str("01531180425")
        password = os.environ.get('password')

        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


def trytopost():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span').click()
    except:
        pass




def activePostAreaAndPostInPage():
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys("'driver.switch_to.active_element' "
                               "this code is a one of important snippet for facebook automation.")

    actions.perform()
    print("Writing Post in the post area Successfully ")

    for i in range(2):
        driver.implicitly_wait(implicitlyWaitTime)
        actions.send_keys(Keys.TAB * 5)
        print(str(i) + " tabs Working")
    #actions.send_keys(Keys.ENTER)
    actions.perform()
    try:
        driver.find_element_by_xpath("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Post']").click()
        print("Click post button working")
    except:
        print("NOrmal xpath is'nt working")
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/span/span").click()
        print("2nd xpath working")






chrome_options()
driver()
actions()
login()
time.sleep(5)
driver.get("https://www.facebook.com/groups/601242797290982")
time.sleep(5)
trytopost()
time.sleep(2)
activePostAreaAndPostInPage()




