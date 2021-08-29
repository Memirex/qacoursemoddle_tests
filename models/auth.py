from faker import Faker

fake_ru = Faker("Ru-ru")


class AuthData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake_ru.email()
        password = fake_ru.password()
        return AuthData(login, password)
