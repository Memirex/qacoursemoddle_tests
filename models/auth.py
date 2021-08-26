from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)


class EditProfileData:
    def __init__(self, username="mem"):
        self.username = username

    # @staticmethod
    # def random():
    #     username = "memiii"
    #     return EditProfileData(username)
