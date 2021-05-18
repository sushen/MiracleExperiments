import option
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver():
    """ This class will take care of Driver Call """

    def __init__(self, driver):
        self.driver = driver

    def chrome_options(self):
        global chrome_options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--profile-directory=Default')
        # chrome_options.add_argument("--user-data-dir=chrome-data")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])


    def driver(self):
        global driver
        driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
        # driver.get("https://facebook.com")

