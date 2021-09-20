from selenium.webdriver.common.by import By


class EditProfileLocators:
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")
    USERNAME = (By.ID, "id_username")
    SAVE_CHANGE = (By.CLASS_NAME, "alert-success")
    FIRSTNAME = (By.ID, "id_firstname")
    LASTNAME = (By.ID, "id_lastname")
    EMAIL = (By.ID, "id_email")
    EMAIL_DISPLAY = (By.ID, "id_maildisplay")
    MOODLE_NET = (By.ID, "id_moodlenetprofile")
    CITY = (By.ID, "id_city")
    SELECT_COUNTRY = (By.ID, "id_country")
    TIMEZONE = (By.ID, "id_timezone")
    DESCRIPTION = (By.ID, "id_description_editoreditable")
    PICTURE_DESCRIPTION = (By.ID, "id_imagealt")
    SUBMIT_ADD_BUTTON = (By.CSS_SELECTOR, "#id_moodle_additional_names a")
    FIRSTNAME_PHO = (By.ID, "id_firstnamephonetic")
    SURNAME_PHO = (By.ID, "id_lastnamephonetic")
    MIDDLE_NAME = (By.ID, "id_middlename")
    ALTERNATE_NAME = (By.ID, "id_alternatename")
    SUBMIT_INT_BUTTON = (By.CSS_SELECTOR, "#id_moodle_interests a")
    TAGS = (By.CSS_SELECTOR, "#id_moodle_interests div .form-control")
    SUBMIT_OPT_BUTTON = (By.CSS_SELECTOR, "#id_moodle_optional a")
    ID_NUMBER = (By.ID, "id_idnumber")
    INSTITUTION = (By.ID, "id_institution")
    DEPARTAMENT = (By.ID, "id_department")
    PHONE = (By.ID, "id_phone1")
    MOBILE_PHONE = (By.ID, "id_phone2")
    ADDRESS = (By.ID, "id_address")
    USER_IMAGE_FILE_ADD_BUTTON = (By.CLASS_NAME, "fp-btn-add")
    DOWNLOAD_FILE_SECTION = (By.XPATH, "//span[text()='Загрузить файл']")
    USER_IMAGE_FILE_CHOOSE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    DOWNLOAD_FILE_BUTTON = (By.CLASS_NAME, "fp-upload-btn")
    EMPTY_FIRSTNAME_ERROR = (By.ID, "id_error_firstname")
    EMPTY_LASTNAME_ERROR = (By.ID, "id_error_lastname")
    EMPTY_EMAIL_ERROR = (By.ID, "id_error_email")
