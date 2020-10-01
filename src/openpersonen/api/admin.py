from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from .demo_models import Kind, Ouder, Persoon
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


class KindInline(admin.TabularInline):
    model = Kind
    extra = 0
    fields = (
        "burgerservicenummer_kind",
        "voornamen_kind",
        "geslachtsnaam_kind",
        "geboortedatum_kind",
    )


class OuderInline(admin.TabularInline):
    model = Ouder
    extra = 0
    fields = (
        "burgerservicenummer_ouder",
        "voornamen_ouder",
        "geslachtsnaam_ouder",
        "geboortedatum_ouder",
    )


@admin.register(Persoon)
class PersoonAdmin(admin.ModelAdmin):
    list_display = (
        "burgerservicenummer_persoon",
        "voornamen_persoon",
        "geslachtsnaam_persoon",
    )

    inlines = [KindInline, OuderInline]

    fieldsets = (
        (
            _("Info"),
            {
                "fields": (
                    "burgerservicenummer_persoon",
                    "voornamen_persoon",
                    "geslachtsnaam_persoon",
                    "geboortedatum_persoon",
                    "geslachtsaanduiding",
                )
            },
        ),
    )

    def save_formset(self, request, form, formset, change):
        for form in formset.forms:
            instance = form.instance
            if instance.pk is None and isinstance(instance, Kind):
                instance.save()
                persoon_instance, is_new = Persoon.objects.get_or_create(
                    burgerservicenummer_persoon=instance.burgerservicenummer_kind
                )
                if is_new:
                    persoon_instance.voornamen_persoon = instance.voornamen_kind
                    persoon_instance.geslachtsnaam_persoon = instance.geslachtsnaam_kind
                    persoon_instance.geboortedatum_persoon = instance.geboortedatum_kind
                    persoon_instance.save()

                Ouder.objects.create(
                    persoon=persoon_instance,
                    burgerservicenummer_ouder=instance.persoon.burgerservicenummer_persoon,
                    voornamen_ouder=instance.persoon.voornamen_persoon,
                    geslachtsnaam_ouder=instance.persoon.geslachtsnaam_persoon,
                    geboortedatum_ouder=instance.persoon.geboortedatum_persoon,
                )
            if instance.pk is None and isinstance(instance, Ouder):
                instance.save()
                persoon_instance, is_new = Persoon.objects.get_or_create(
                    burgerservicenummer_persoon=instance.burgerservicenummer_ouder
                )
                if is_new:
                    persoon_instance.voornamen_persoon = instance.voornamen_ouder
                    persoon_instance.geslachtsnaam_persoon = (
                        instance.geslachtsnaam_ouder
                    )
                    persoon_instance.geboortedatum_persoon = (
                        instance.geboortedatum_ouder
                    )
                    persoon_instance.save()

                Kind.objects.create(
                    persoon=persoon_instance,
                    burgerservicenummer_kind=instance.persoon.burgerservicenummer_persoon,
                    voornamen_kind=instance.persoon.voornamen_persoon,
                    geslachtsnaam_kind=instance.persoon.geslachtsnaam_persoon,
                    geboortedatum_kind=instance.persoon.geboortedatum_persoon,
                )

        formset.save()
