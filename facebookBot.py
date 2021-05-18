import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")

    def login(self):
        self.driver.get("https://facebook.com")
        try:
            # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
            username = os.environ.get('my_facebook_username')
            password = os.environ.get('my_facebook_password')

            self.driver.find_element_by_name("email").send_keys(username)
            self.driver.find_element_by_name("pass").send_keys(password)
            self.driver.find_element_by_name("login").click()
            print(input("Press any Key: "))
            print("Login work Successfully ")

        except:
            pass
