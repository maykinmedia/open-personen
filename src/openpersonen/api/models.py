import base64
import uuid
from datetime import timedelta

from django.db import models
from django.template import loader
from django.utils import dateformat, timezone
from django.utils.translation import ugettext_lazy as _

import requests
from solo.models import SingletonModel


class StufBGClient(SingletonModel):

    ontvanger_organisatie = models.CharField(_("organisatie"), max_length=200)
    ontvanger_administratie = models.CharField(_("administratie"), max_length=200)
    ontvanger_applicatie = models.CharField(_("applicatie"), max_length=200)
    ontvanger_gebruiker = models.CharField(_("gebruiker"), max_length=200)
    zender_organisatie = models.CharField(_("organisatie"), max_length=200)
    zender_administratie = models.CharField(_("administratie"), max_length=200)
    zender_applicatie = models.CharField(_("applicatie"), max_length=200)
    zender_gebruiker = models.CharField(_("gebruiker"), max_length=200)
    url = models.URLField(_("url"))
    user = models.CharField(_("user"), max_length=200)
    password = models.CharField(_("password"), max_length=200)

    class Meta:
        verbose_name = _("Stuf BG Client")

    def _get_headers(self):
        credentials = f"{self.user}:{self.password}".encode("utf-8")
        encoded_credentials = base64.b64encode(credentials).decode("utf-8")
        return {
            "Authorization": "Basic " + encoded_credentials,
            "Content-Type": "application/soap+xml",
        }

    def _get_request_base_context(self):
        return {
            "created": timezone.now(),
            "expired": timezone.now() + timedelta(minutes=5),
            "username": self.user,
            "password": self.password,
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
            headers=self._get_headers(),
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
            headers=self._get_headers(),
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
            self.url,
            data=loader.render_to_string("RequestOuder.xml", request_context),
            headers=self._get_headers(),
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
            headers=self._get_headers(),
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

    def get_verblijf_plaats_historie(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({"bsn": bsn})

        response = requests.post(
            settings.STUF_BG_URL,
            data=loader.render_to_string("RequestVerblijfPlaatsHistorie.xml", request_context),
            headers=settings.STUF_BG_HEADERS,
        )

        response_context = self._get_response_base_context()
        response_context["referentienummer"] = request_context["referentienummer"]
        response_context["tijdstip_bericht"] = request_context["tijdstip_bericht"]

        response._content = bytes(
            loader.render_to_string("ResponseVerblijfPlaatsHistorie.xml", response_context),
            encoding="utf-8",
        )

        return response
