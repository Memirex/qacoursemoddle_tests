from locators.admin_page_locators import AdminPageLocators
from pages.base_page import BasePage


class AdminPage(BasePage):
    def open_admin_page(self):
        self.click_element(self.find_element(AdminPageLocators.ADMIN_PAGE))

    def open_courses(self):
        self.open_admin_page()
        self.click_element(self.find_element(AdminPageLocators.COURSES_PAGE))

    def add_new_course(self):
        self.open_courses()
        self.click_element(self.find_element(AdminPageLocators.ADD_COURSE))

    def manage_courses(self):
        self.open_courses()
        self.click_element(self.find_element(AdminPageLocators.MANAGE_COURSE))
