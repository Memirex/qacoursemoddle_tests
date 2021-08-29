import pytest

from common.constants import LoginConstants
from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, auth, app):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        """
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, auth, app):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert LoginConstants.ERROR_MESSAGE == app.login.is_not_auth(), "Input correct values"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps
        1. Open auth page
        2. Auth with empty data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        assert LoginConstants.ERROR_MESSAGE == app.login.is_not_auth(), "Input correct values"
