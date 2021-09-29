from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import time

class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = locators.SignInPageLocator
        super(SignInPage, self).__init__(driver)

    def signIn(self, email, password):
        self.find_element2(*self.locator.email).send_keys(email)
        self.find_element2(*self.locator.password).send_keys(password)
        self.find_element2(*self.locator.signInBtn).click()

    def signin(self):
        self.signIn(testcase_data.account[0], testcase_data.password[0])

    def click_account_button(self):
        self.click(*self.locator.account_button)

    def click_log_out_button(self):
        self.click(*self.locator.log_out_button)

    def switch_account(self, i):
        self.click_account_button()
        self.click_account_button()
        time.sleep(10)
        self.signIn(testcase_data.account[i], testcase_data.password[i])

