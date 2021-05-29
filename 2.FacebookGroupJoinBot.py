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
    if driver.find_elements_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ri2l8tne ph5uu5jm b3onmgus gloz99to r516eku6 k83vx86k']//div//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Join Group']"):
        print("xpath found")
        if driver.find_elements_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ri2l8tne ph5uu5jm b3onmgus gloz99to r516eku6 k83vx86k']//div//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Join Group']"):
            driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ri2l8tne ph5uu5jm b3onmgus gloz99to r516eku6 k83vx86k']//div//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Join Group']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi']//div[@class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 nnctdnn4 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr']//div[@class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz qt6c0cv9 rz4wbd8a a8nywdso jb3vyjys du4w35lb bp9cbjyn btwxx1t3 l9j0dhe7']//div[@class='n851cfcs ozuftl9m n1l5q3vz l9j0dhe7 o8rfisnq']//div[@class='bp9cbjyn j83agx80 btwxx1t3']//div//div[@role='radio']").click()
            driver.switch_to.active_element
            time.sleep(1)
            driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 tkv8g59h fl8dtwsd s1i5eluu tv7at329']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Join Group']").click()
        else:
            driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 tkv8g59h fl8dtwsd s1i5eluu tv7at329']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][normalize-space()='Join Group']").click()

    else:
        print("xpath not found")


driver()
login()


groupLists = [
    "https://www.facebook.com/groups/pythonbd/",
    "https://www.facebook.com/groups/210517586045027/",
    "https://www.facebook.com/groups/142201439713193/",
    "https://www.facebook.com/groups/pythonprogrammingbeginners/",
    "https://www.facebook.com/groups/HTML.CSSandJavaScript/",
    "https://www.facebook.com/groups/308915099815447/",
    "https://www.facebook.com/groups/DeepNetGroup/",
    "https://www.facebook.com/groups/programming.school/",
    "https://www.facebook.com/groups/632595694006151/",
    "https://www.facebook.com/groups/bengaliprogramming/",
    "https://www.facebook.com/groups/machine.learning.bangladesh/",
    "https://www.facebook.com/groups/pirawenpython/",
    "https://www.facebook.com/groups/1914592312155348/",
    "https://www.facebook.com/groups/699038760180241/"


]

for groupLinkList in groupLists:
    driver.get(groupLinkList)
    print(groupLinkList + " link")
    time.sleep(5)

    navigateGroupJoinBtn()
    time.sleep(30)
