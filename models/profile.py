import random

from faker import Faker

from common.constants import ProfileConstants

fake_ru = Faker("Ru-ru")


class EditRequiredData:
    def __init__(self, firstname=None, lastname=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    @staticmethod
    def random():
        firstname = fake_ru.first_name()
        lastname = fake_ru.last_name()
        email = fake_ru.email()
        return EditRequiredData(firstname, lastname, email)


class EditOptionalData:
    def __init__(
        self,
        username="mem",
        moodle_net_profile=None,
        city=None,
        description=None,
        picture_description=None,
        firstname_pho=None,
        surname_pho=None,
        middle_name=None,
        alternate_name=None,
        tags=None,
        id_number=None,
        institution=None,
        departament=None,
        phone=None,
        mobile_phone=None,
        address=None,
    ):
        self.username = username
        self.moodle_net_profile = moodle_net_profile
        self.city = city
        self.description = description
        self.picture_description = picture_description
        self.firstname_pho = firstname_pho
        self.surname_pho = surname_pho
        self.middle_name = middle_name
        self.alternate_name = alternate_name
        self.tags = tags
        self.id_number = id_number
        self.institution = institution
        self.departament = departament
        self.phone = phone
        self.mobile_phone = mobile_phone
        self.address = address

    @staticmethod
    def random():
        username = "mem"
        moodle_net_profile = fake_ru.url()
        city = fake_ru.city()
        description = fake_ru.text(max_nb_chars=200)
        picture_description = fake_ru.text(max_nb_chars=100)
        firstname_pho = fake_ru.first_name()
        surname_pho = fake_ru.last_name()
        middle_name = fake_ru.name()
        alternate_name = fake_ru.name()
        tags = fake_ru.name()
        id_number = fake_ru.random_number()
        institution = fake_ru.name()
        departament = fake_ru.name()
        phone = fake_ru.random_number()
        mobile_phone = fake_ru.random_number()
        address = fake_ru.name()
        return EditOptionalData(
            username,
            moodle_net_profile,
            city,
            description,
            picture_description,
            firstname_pho,
            surname_pho,
            middle_name,
            alternate_name,
            tags,
            id_number,
            institution,
            departament,
            phone,
            mobile_phone,
            address,
        )


class EditEmailTimeCountry:
    def __init__(
        self,
        email_display=None,
        country_code=None,
        timezone=None
    ):
        self.email_display = email_display
        self.country_code = country_code
        self.timezone = timezone

    @staticmethod
    def random():
        email_display = random.choice(
            list(ProfileConstants.EMAIL_DISPLAY_CHOICE.values())
        )
        country_code = fake_ru.country_code()
        timezone = random.choice(ProfileConstants.TIMEZONE_CHOICE)
        return EditEmailTimeCountry(email_display, country_code, timezone)
