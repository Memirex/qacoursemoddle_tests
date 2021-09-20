import os

import pytest

from common.constants import ProfileConstants
from models.profile import EditRequiredData, EditOptionalData, EditEmailTimeCountry

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


class TestProfile:
    def test_valid_change_required_fields(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit required fields with valid data
        6. Check successfully editing
        """
        ep_data = EditRequiredData().random()
        app.profile.edit_required_fields(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["firstname", "lastname", "email"])
    def test_invalid_change_required_fields(self, app, field, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit required fields with invalid data
        6. Check error editing
        """
        ep_data = EditRequiredData().random()
        setattr(ep_data, field, None)
        app.profile.edit_required_fields(ep_data)
        assert (
            not app.profile.all_required_fields_filled()
        ), "Empty fields are ignored and user data changed successfully!"

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
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit optional fields
        6. Check successfully editing
        """
        ep_data = EditOptionalData().random()
        setattr(ep_data, field, None)
        app.profile.edit_optional_fields(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()

    @pytest.mark.parametrize(
        "field",
        [
            "email_display",
            "country_code",
            "timezone"
        ]
    )
    def test_optional_fields_valid2(self, app, field, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit choosing values
        6. Check successfully editing
        """
        ep_data = EditEmailTimeCountry.random()
        app.profile.edit_email_country_time(ep_data)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()

    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_user_image(self, app, image_file, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit image file
        6. Check successfully editing
        """
        app.profile.choose_user_image_file(image_file)
        assert ProfileConstants.CORRECT_MESSAGE == app.profile.save_change()
