import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib



def driver():
    global driver
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://facebook.com")


def chrome_options():
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
    driver.get()

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







def deletepost():
    driver.get('https://www.facebook.com/groups/601242797290982/permalink/993654051383186/')
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)
    driver.find_element_by_xpath("//div[@aria-label='Actions for this post']").click()
    driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    driver.find_element_by_xpath("//span[normalize-space()='Delete post']").click()
    time.sleep(2)
    #driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p bwm1u5wc']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Delete']").click()



def editpost():
    driver.get('https://www.facebook.com/groups/601242797290982/permalink/993654051383186/')
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)
    driver.find_element_by_xpath("//div[@aria-label='Actions for this post']").click()
    driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    driver.find_element_by_xpath("//span[normalize-space()='Edit post']").click()
    time.sleep(2)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys("'driver.switch_to.active_element' "
                               "this code is a one of important snippet for facebook automation.")

    actions.perform()
    print("  Writing Post EDIT in the post area Successfully ")
    driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
















#TODO : Edith the post

#TODO : Delet the Post


chrome_options()
driver()
actions()
login()
deletepost()





