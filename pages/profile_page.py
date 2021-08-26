from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import EditProfileLocators
from models.auth import EditProfileData
from pages.base_page import BasePage


class ProfilePage(BasePage):

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
