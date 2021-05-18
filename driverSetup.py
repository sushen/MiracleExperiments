#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest


class DriverSetup:

    def driver(self):
        global driver
        driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)

    def browser(self):
        global chrome_options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("user-data-dir=chrome-data")
        chrome_options.add_argument('--profile-directory=Default')
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    def keybordAction(self):
        global actions
        actions = ActionChains(driver)

if __name__ == "__main__":
    unittest.main()
