#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

from driverSetup import DriverSetup
from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest


class ProfilePost(unittest.TestCase):
    def setUp(self):
        global driver
        global chrome_options
        global actions
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
        chrome_options.add_argument("user-data-dir=chrome-data")
        chrome_options.add_argument('--profile-directory=Default')
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        actions = ActionChains(driver)
        driver.get("https://facebook.com")

    def test_login(self):

        try:
            # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
            username = os.environ.get('my_facebook_username')
            password = os.environ.get('my_facebook_password')

            driver.find_element_by_name("email").send_keys(username)
            driver.find_element_by_name("pass").send_keys(password)
            driver.find_element_by_name("login").click()

        except:
            pass
            print(input("Press any Key: "))

    def test_navigatePage(self):
        self.test_login()
        driver.get("https://www.facebook.com/sushen.biswas/")
        print(input("Press any Key: "))
        driver.implicitly_wait(5)
        actions.send_keys(Keys.BACK_SPACE)
        actions.send_keys(Keys.TAB * 56)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print(input("Press any Key: "))

    def test_postInpage(self):
        self.test_login()
        self.test_navigatePage()
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
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
