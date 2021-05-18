from selenium.webdriver.chrome.options import Options


class Option():
    """ This class will take care of Option  """

    def __init__(self, chrome_options):
        self.chrome_options = chrome_options

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
