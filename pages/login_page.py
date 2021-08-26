from locators.login_page_locators import LoginPageLocators, EditProfileLocators
from models.auth import AuthData, EditProfileData
from pages.base_page import BasePage

from selenium.webdriver.remote.webelement import WebElement


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

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def is_not_auth(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def open_toolbar(self):
        return self.click_element(self.find_element(LoginPageLocators.LOGIN_TOOLBAR))

    def open_options(self):
        self.open_toolbar()
        self.click_element(self.find_element(LoginPageLocators.LOGIN_OPTIONS))

    def edit_profile(self):
        self.open_options()
        self.click_element(self.find_element(LoginPageLocators.OPTIONS_EDIT_PROFILE))

    def edit_username(self, data: EditProfileData):
        self.edit_profile()
        self.fill_element(self.find_element(EditProfileLocators.EDIT_USERNAME), data.username)
        self.click_element(self.find_element(EditProfileLocators.SUBMIT_BUTTON))

    def save_change(self) -> str:
        return self.find_element(EditProfileLocators.SAVE_CHANGE).text

