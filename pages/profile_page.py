import logging
import time

from common.constants import ProfileConstants
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import EditProfileLocators
from models.profile import EditRequiredData, EditOptionalData, EditEmailTimeCountry
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


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

    def email_display(self):
        return self.find_select_element(EditProfileLocators.EMAIL_DISPLAY)

    def moodle_net_profile(self):
        return self.find_element(EditProfileLocators.MOODLE_NET)

    def city(self):
        return self.find_element(EditProfileLocators.CITY)

    def select_country(self):
        return self.find_select_element(EditProfileLocators.SELECT_COUNTRY)

    def timezone(self):
        return self.find_select_element(EditProfileLocators.TIMEZONE)

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

    def profile_button(self):
        return self.find_element(EditProfileLocators.SUBMIT_BUTTON)

    def update_profile_button(self):
        self.click_element(self.profile_button())

    def user_image_file_add_button(self):
        return self.find_clickable_element(
            EditProfileLocators.USER_IMAGE_FILE_ADD_BUTTON
        )

    def download_file_section(self):
        return self.find_clickable_element(
            EditProfileLocators.DOWNLOAD_FILE_SECTION
        )

    def user_image_file_choose_input(self):
        return self.find_clickable_element(
            EditProfileLocators.USER_IMAGE_FILE_CHOOSE_INPUT
        )

    def download_file_button(self):
        return self.find_clickable_element(
            EditProfileLocators.DOWNLOAD_FILE_BUTTON
        )

    def edit_required_fields(self, data: EditRequiredData):
        logger.info(
            f"Editing basic personal data with next values:\n"
            f"name: {data.firstname}\n"
            f"lastname: {data.lastname}\n"
            f"email: {data.email}\n"
        )
        self.edit_profile()
        self.fill_element(self.firstname(), data.firstname)
        self.fill_element(self.lastname(), data.lastname)
        self.fill_element(self.email(), data.email)
        self.update_profile_button()

    def edit_optional_fields(self, data: EditOptionalData):
        logger.info(
            f"Editing basic personal data with next values:\n"
            f"name: {data.moodle_net_profile}\n"
            f"lastname: {data.city}\n"
            f"email: {data.description}\n"
            f"moodle_net_profile: {data.picture_description}\n"
            f"city: {data.firstname_pho}\n"
            f"country_code: {data.surname_pho}\n"
            f"timezone: {data.middle_name}\n"
            f"about: {data.alternate_name}\n"
            f"lastname: {data.tags}\n"
            f"email: {data.id_number}\n"
            f"moodle_net_profile: {data.institution}\n"
            f"city: {data.departament}\n"
            f"country_code: {data.phone}\n"
            f"timezone: {data.mobile_phone}\n"
            f"about: {data.address}\n"
        )
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
        self.update_profile_button()

    def edit_email_country_time(self, data: EditEmailTimeCountry):
        logger.info(
            f"Editing basic personal data with next values:\n"
            f"name: {data.email_display}\n"
            f"lastname: {data.country_code}\n"
            f"email: {data.timezone}\n"
        )
        self.edit_profile()
        self.select_value(self.email_display(), data.email_display)
        self.select_value(self.select_country(), data.country_code)
        self.select_value(self.timezone(), data.timezone)
        self.update_profile_button()

    def choose_user_image_file(self, image_file):
        self.edit_profile()
        self.click_element(self.user_image_file_add_button())
        self.click_element(self.download_file_section())
        self.fill_element(self.user_image_file_choose_input(), image_file)
        self.click_element(self.download_file_button())
        time.sleep(3)
        self.update_profile_button()

    def save_change(self) -> str:
        return self.find_element(EditProfileLocators.SAVE_CHANGE).text

    def all_required_fields_filled(self):
        empty_first_name_field_error = self.find_element(
            EditProfileLocators.EMPTY_FIRSTNAME_ERROR
        ).text
        empty_last_name_field_error = self.find_element(
            EditProfileLocators.EMPTY_LASTNAME_ERROR
        ).text
        empty_email_field_error = self.find_element(
            EditProfileLocators.EMPTY_EMAIL_ERROR
        ).text

        if (
            ProfileConstants.EMPTY_NAME_FIELD_MESSAGE in empty_first_name_field_error
            or ProfileConstants.EMPTY_NAME_FIELD_MESSAGE in empty_last_name_field_error
            or ProfileConstants.EMPTY_EMAIL_FIELD_MESSAGE in empty_email_field_error
        ):
            return False
        return True
