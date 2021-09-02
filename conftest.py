import logging

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_type = request.config.getoption("--headless").lower()
    logger.info(f"Start moodle {base_url} with headless = {headless_type}")
    if headless_type:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        fixture = Application(
            webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            ),
            base_url,
        )
    else:
        fixture = Application(webdriver.Chrome(ChromeDriverManager().install()),
                              base_url)
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    data = AuthData(login=user, password=password)
    app.login.auth(data)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--username", action="store", default="mem", help="enter username"
    ),
    parser.addoption(
        "--password", action="store", default="Qwerty123#", help="enter password"
    )
    parser.addoption(
        "--headless", action="store", default="true",
        help="Input 'true' if you are running test a headless type,"
             " 'false' if you not"
    )
