from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


def update_admin_index(sender, **kwargs):
    from django_admin_index.models import AppGroup

    AppGroup.objects.all().delete()
    call_command("loaddata", "default_admin_index", verbosity=0)


class AccountsConfig(AppConfig):
    name = "openpersonen.accounts"

    def ready(self):
        post_migrate.connect(update_admin_index, sender=self)
