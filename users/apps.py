from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Starts signals to create profile.
    def ready(self):
        import users.signals
