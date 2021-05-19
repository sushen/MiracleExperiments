from selenium import webdriver
import pyautogui

brower = webdriver.Chrome(executable_path="./chromedriver.exe")


def foo():
    website_URL = "https://facebook.com"
    brower.get(website_URL)
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    pyautogui.typewrite('admin')
    # pyautogui.press('enter')

    # pyautogui.typewrite('12345')
    pyautogui.press('tab')
    pyautogui.typewrite('admin')
    pyautogui.press('enter')


foo()
