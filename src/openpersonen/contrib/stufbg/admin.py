from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from privates.admin import PrivateMediaMixin
from solo.admin import SingletonModelAdmin

from openpersonen.contrib.stufbg.models import StufBGClient


@admin.register(StufBGClient)
class StufBGClientAdmin(PrivateMediaMixin, SingletonModelAdmin):
    private_media_fields = (
        "certificate",
        "certificate_key",
    )

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
        (
            _("Certificate"),
            {
                "fields": (
                    "certificate",
                    "certificate_key",
                )
            },
        ),
    )
