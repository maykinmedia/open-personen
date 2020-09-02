import uuid

from django.conf import settings
from django.template import loader
from django.utils import dateformat, timezone

import requests

from openpersonen.config.models import StufBGConfig


class Client:

    def __init__(self):
        config = StufBGConfig.get_solo()
        self.url = config.url
        self.zender_organisatie = config.zender_organisatie
        self.zender_applicatie = config.zender_applicatie
        self.zender_administratie = config.zender_administratie
        self.zender_gebruiker = config.zender_gebruiker
        self.ontvanger_organisatie = config.ontvanger_organisatie
        self.ontvanger_applicatie = config.ontvanger_applicatie
        self.ontvanger_administratie = config.ontvanger_administratie
        self.ontvanger_gebruiker = config.ontvanger_gebruiker

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


client = Client()
