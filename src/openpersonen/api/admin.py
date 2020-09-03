from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from .models import StufBGClient


@admin.register(StufBGClient)
class StufBGClientAdmin(SingletonModelAdmin):
    # Details
    fieldsets = (
        (
            _("Ontvanger"),
            {
                "fields": (
                    "ontvanger_organisatie",
                    "ontvanger_administratie",
                    "ontvanger_applicatie",
                    "ontvanger_gebruiker",
                )
            },
        ),
        (
            _("Zender"),
            {
                "fields": (
                    "zender_organisatie",
                    "zender_administratie",
                    "zender_applicatie",
                    "zender_gebruiker",
                )
            },
        ),
        (
            _("Service"),
            {
                "fields": (
                    "url",
                    "user",
                    "password",
                )
            },
        ),
    )
