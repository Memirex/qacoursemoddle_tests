from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import EditProfileLocators
from models.profile import EditRequiredData, EditOptionalData
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

    def firstname(self):
        return self.find_element(EditProfileLocators.FIRSTNAME)

    def lastname(self):
        return self.find_element(EditProfileLocators.LASTNAME)

    def email(self):
        return self.find_element(EditProfileLocators.EMAIL)

    def username(self):
        return self.find_element(EditProfileLocators.USERNAME)

    def moodle_net_profile(self):
        return self.find_element(EditProfileLocators.MOODLE_NET)

    def city(self):
        return self.find_element(EditProfileLocators.CITY)

    def description(self):
        return self.find_element(EditProfileLocators.DESCRIPTION)

    def picture_description(self):
        return self.find_element(EditProfileLocators.PICTURE_DESCRIPTION)

    def open_additional_names(self):
        button = self.find_element(EditProfileLocators.SUBMIT_ADD_BUTTON)
        self.click_element(button)

    def firstname_pho(self):
        self.open_additional_names()
        return self.find_element(EditProfileLocators.FIRSTNAME_PHO)

    def surname_pho(self):
        return self.find_element(EditProfileLocators.SURNAME_PHO)

    def middle_name(self):
        return self.find_element(EditProfileLocators.MIDDLE_NAME)

    def alternate_name(self):
        return self.find_element(EditProfileLocators.ALTERNATE_NAME)

    def open_interests(self):
        button = self.find_element(EditProfileLocators.SUBMIT_INT_BUTTON)
        self.click_element(button)

    def tags(self):
        self.open_interests()
        return self.find_element(EditProfileLocators.TAGS)

    def open_optional(self):
        button = self.find_element(EditProfileLocators.SUBMIT_OPT_BUTTON)
        self.click_element(button)

    def id_number(self):
        self.open_optional()
        return self.find_element(EditProfileLocators.ID_NUMBER)

    def institution(self):
        return self.find_element(EditProfileLocators.INSTITUTION)

    def departament(self):
        return self.find_element(EditProfileLocators.DEPARTAMENT)

    def phone(self):
        return self.find_element(EditProfileLocators.PHONE)

    def mobile_phone(self):
        return self.find_element(EditProfileLocators.MOBILE_PHONE)

    def address(self):
        return self.find_element(EditProfileLocators.ADDRESS)

    def update_profile_button(self):
        return self.find_element(EditProfileLocators.SUBMIT_BUTTON)

    def edit_required_fields(self, data: EditRequiredData):
        self.edit_profile()
        self.fill_element(self.firstname(), data.firstname)
        self.fill_element(self.lastname(), data.lastname)
        self.fill_element(self.email(), data.email)
        self.click_element(self.update_profile_button())

    def edit_optional_fields(self, data: EditOptionalData):
        self.edit_profile()
        self.fill_element(self.moodle_net_profile(), data.moodle_net_profile)
        self.fill_element(self.city(), data.city)
        self.fill_element(self.description(), data.description)
        self.fill_element(self.picture_description(), data.picture_description)
        self.fill_element(self.firstname_pho(), data.firstname_pho)
        self.fill_element(self.surname_pho(), data.surname_pho)
        self.fill_element(self.middle_name(), data.middle_name)
        self.fill_element(self.alternate_name(), data.alternate_name)
        self.fill_element(self.tags(), data.tags)
        self.fill_element(self.id_number(), data.id_number)
        self.fill_element(self.institution(), data.institution)
        self.fill_element(self.departament(), data.departament)
        self.fill_element(self.phone(), data.phone)
        self.fill_element(self.mobile_phone(), data.mobile_phone)
        self.fill_element(self.address(), data.address)
        self.click_element(self.update_profile_button())

    def save_change(self) -> str:
        return self.find_element(EditProfileLocators.SAVE_CHANGE).text
