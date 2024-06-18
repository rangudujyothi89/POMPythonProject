from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON  = (By.ID, "login")

    """constructor"""
    def __int__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """This is to get Page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to login application"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_login(self.LOGIN_BUTTON)




