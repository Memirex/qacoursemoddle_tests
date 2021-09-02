import pytest

from common.constants import ProfileConstants
from models.profile import EditRequiredData, EditOptionalData


class TestProfile:
    def test_valid_change_required_fields(self, app, auth):
        ep_data = EditRequiredData().random()
        app.profile.edit_required_fields(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["firstname", "lastname", "email"])
    def test_invalid_change_required_fields(self, app, field, auth):
        ep_data = EditRequiredData().random()
        setattr(ep_data, field, None)
        app.profile.edit_required_fields(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()

    @pytest.mark.parametrize(
        "field",
        [
            "moodle_net_profile",
            "city",
            "description",
            "picture_description",
            "firstname_pho",
            "surname_pho",
            "middle_name",
            "alternate_name",
            "tags",
            "id_number",
            "institution",
            "departament",
            "phone",
            "mobile_phone",
            "address",
        ],
    )
    def test_optional_fields_valid(self, app, field, auth):
        ep_data = EditOptionalData().random()
        setattr(ep_data, field, None)
        app.profile.edit_optional_fields(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()
