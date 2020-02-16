from django.apps import AppConfig


class AwardConfig(AppConfig):
    name = 'award'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals