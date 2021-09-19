from selenium.webdriver.common.by import By


class AdminPageLocators:
    ADMIN_PAGE = (By.CSS_SELECTOR, "a[data-key='sitesettings']")
    COURSES_PAGE = (By.CSS_SELECTOR, "a[href='#linkcourses']")
    ADD_COURSE = (By.XPATH, "//a[text()='Добавить курс']")
    MANAGE_COURSE = (By.XPATH, "//a[text()='Управление курсами и категориями']")
