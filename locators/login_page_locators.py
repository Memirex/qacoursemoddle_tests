from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_EXIT = (By.CSS_SELECTOR, ".singlebutton button")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    LOGIN_TOOLBAR = (By.ID, "action-menu-toggle-1")
    LOGIN_OPTIONS = (By.ID, "actionmenuaction-5")
    OPTIONS_EDIT_PROFILE = (By.CSS_SELECTOR, ".card-text div a:nth-child(1)")
