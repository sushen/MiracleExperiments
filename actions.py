import driver
from selenium.webdriver.common.action_chains import ActionChains


class Actions():
    """ This class will take care of actions Call """

    def __init__(self, actions):
        self.actions = actions

    def actions(self):
        global actions
        actions = ActionChains(driver)
