import logging

from locators.login_page_locators import LoginPageLocators
from models.auth import AuthData
from pages.base_page import BasePage

from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.USERNAME)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN_SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def login_exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN_EXIT)

    def auth(self, data: AuthData):
        logger.info(f'User email is "{data.login}, user password {data.password}"')
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.find_elements(LoginPageLocators.LOGIN_EXIT):
            self.click_element(self.login_exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def is_not_auth(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text
