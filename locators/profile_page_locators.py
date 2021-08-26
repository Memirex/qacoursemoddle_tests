from selenium.webdriver.common.by import By


class EditProfileLocators:
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")
    EDIT_USERNAME = (By.ID, "id_username")
    SAVE_CHANGE = (By.CLASS_NAME, "alert")
