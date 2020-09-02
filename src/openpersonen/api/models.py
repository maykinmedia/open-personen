import uuid

import requests

from django.db import models
from django.template import loader
from django.utils import dateformat, timezone
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class StufBGClient(SingletonModel):

    ontvanger_organisatie = models.CharField(max_length=200)
    ontvanger_administratie = models.CharField(max_length=200)
    ontvanger_applicatie = models.CharField(max_length=200)
    ontvanger_gebruiker = models.CharField(max_length=200)
    zender_organisatie = models.CharField(max_length=200)
    zender_administratie = models.CharField(max_length=200)
    zender_applicatie = models.CharField(max_length=200)
    zender_gebruiker = models.CharField(max_length=200)
    url = models.URLField(
        default="http://fieldlab.westeurope.cloudapp.azure.com:8081/brp/",
        help_text="URL to access Stuf-BG"
    )
    user = models.CharField(
        max_length=200, default="admin", help_text="Username for accessing Stuf-BG"
    )
    password = models.CharField(
        max_length=200, default="admin", help_text="Password for accessing Stuf-BG"
    )

    class Meta:
        verbose_name = _("Stuf BG Config")

    def _get_request_base_context(self):
        return {
            "zender_organisatie": self.zender_organisatie,
            "zender_applicatie": self.zender_applicatie,
            "zender_administratie": self.zender_administratie,
            "zender_gebruiker": self.zender_gebruiker,
            "ontvanger_organisatie": self.ontvanger_organisatie,
            "ontvanger_applicatie": self.ontvanger_applicatie,
            "ontvanger_administratie": self.ontvanger_administratie,
            "ontvanger_gebruiker": self.ontvanger_gebruiker,
            "referentienummer": str(uuid.uuid4()),
            "tijdstip_bericht": dateformat.format(timezone.now(), "YmdHis"),
        }

    def _get_response_base_context(self):
        return {
            "zender_organisatie": self.ontvanger_organisatie,
            "zender_applicatie": self.ontvanger_applicatie,
            "zender_administratie": self.ontvanger_administratie,
            "zender_gebruiker": self.ontvanger_gebruiker,
            "ontvanger_organisatie": self.zender_organisatie,
            "ontvanger_applicatie": self.zender_applicatie,
            "ontvanger_administratie": self.zender_administratie,
            "ontvanger_gebruiker": self.zender_gebruiker,
        }

    def get_ingeschreven_persoon(self, bsn=None, filters=None):
        request_context = self._get_request_base_context()
        if bsn:
            request_context.update({"bsn": bsn})
        if filters:
            request_context.update(filters)

        response = requests.post(
            self.url,
            data=loader.render_to_string(
                "RequestIngeschrevenPersoon.xml", request_context
            ),
        )

        response_context = self._get_response_base_context()
        response_context["referentienummer"] = request_context["referentienummer"]
        response_context["tijdstip_bericht"] = request_context["tijdstip_bericht"]

        response._content = bytes(
            loader.render_to_string(
                "ResponseIngeschrevenPersoon.xml", response_context
            ),
            encoding="utf-8",
        )

        return response

    def get_kind(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({"bsn": bsn})

        response = requests.post(
            self.url,
            data=loader.render_to_string("RequestKind.xml", request_context),
        )

        response_context = self._get_response_base_context()
        request_context.update({"bsn": bsn})
        response_context["referentienummer"] = request_context["referentienummer"]
        response_context["tijdstip_bericht"] = request_context["tijdstip_bericht"]

        response._content = bytes(
            loader.render_to_string("ResponseKind.xml", response_context),
            encoding="utf-8",
        )

        return response

    def get_ouder(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({"bsn": bsn})

        response = requests.post(
            self.url, data=loader.render_to_string("RequestOuder.xml", request_context),
        )

        response_context = self._get_response_base_context()
        request_context.update({"bsn": bsn})
        response_context["referentienummer"] = request_context["referentienummer"]
        response_context["tijdstip_bericht"] = request_context["tijdstip_bericht"]

        response._content = bytes(
            loader.render_to_string("ResponseOuder.xml", response_context),
            encoding="utf-8",
        )

        return response

    def get_partner(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({"bsn": bsn})

        response = requests.post(
            self.url,
            data=loader.render_to_string("RequestPartner.xml", request_context),
        )

        response_context = self._get_response_base_context()
        request_context.update({"bsn": bsn})
        response_context["referentienummer"] = request_context["referentienummer"]
        response_context["tijdstip_bericht"] = request_context["tijdstip_bericht"]

        response._content = bytes(
            loader.render_to_string("ResponsePartner.xml", response_context),
            encoding="utf-8",
        )

        return response


client = StufBGClient.get_solo()
