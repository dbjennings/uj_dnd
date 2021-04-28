from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "uj_dnd.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import uj_dnd.users.signals  # noqa F401
        except ImportError:
            pass
