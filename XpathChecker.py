from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import ctypes

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://google.com")

def Mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 1)


def XpathChecker(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        print('yes xpath is found')
    except NoSuchElementException:
        print("the xpath is not found")
        Mbox('Xpath not found', 'sorry! xpath is not found')


XpathChecker("//dv[@class='FPdoLc lJ9FBc']//input[@name='btnI']")
