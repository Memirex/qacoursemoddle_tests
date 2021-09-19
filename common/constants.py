class LoginConstants:
    ERROR_MESSAGE = "Неверный логин или пароль, попробуйте заново."
    LOGIN_EXIT_MESSAGE = "Выход"


class ProfileConstants:
    CORRECT_MESSAGE = "×\nИзменения сохранены"
    EMAIL_DISPLAY_CHOICE = {
        "hidden": "0",
        "see_everyone": "1",
        "course_only_see": "2"
    }
    TIMEZONE_CHOICE = [
        "99",  # Server timezone
        "Africa/Tripoli",
        "America/Detroit",
        "Pacific/Honolulu",
        "UTC"
    ]


class CreateCourseConstants:
    SECTION_NUMBER = 52
    COURSE_LANGUAGE = "ru"
    CURRENT_YEAR = 2021
    LAST_YEAR = 2050
    FILE_SIZES_VALUES = [
        0,
        2097152,
        1048576,
        512000,
        102400,
        51200,
        10240,
    ]
