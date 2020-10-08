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
    certificate = models.FileField(upload_to="certificate/")
    certificate_key = models.FileField(
        upload_to="certificate/", help_text="Private key for the certificate"
    )

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

    def _make_request(self, request_file, additional_context=None):
        request_context = self._get_request_base_context()
        if additional_context:
            request_context.update(additional_context)

        response = requests.post(
            self.url,
            data=loader.render_to_string(request_file, request_context),
            headers=self._get_headers(),
            cert=(self.certificate.path, self.certificate_key.path),
        )

        return response

    def get_ingeschreven_persoon(self, bsn=None, filters=None):
        additional_context = dict()
        if bsn:
            additional_context.update({"bsn": bsn})
        if filters:
            additional_context.update(filters)

        return self._make_request(
            "RequestIngeschrevenPersoon.xml",
            additional_context=additional_context,
        )

    def get_kind(self, bsn):
        return self._make_request("RequestKind.xml", additional_context={"bsn": bsn})

    def get_ouder(self, bsn):
        return self._make_request("RequestOuder.xml", additional_context={"bsn": bsn})

    def get_partner(self, bsn):
        return self._make_request("RequestPartner.xml", additional_context={"bsn": bsn})

    def get_verblijf_plaats_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_request(
            "RequestVerblijfPlaatsHistorie.xml",
            additional_context=additional_context,
        )

    def get_partner_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_request(
            "RequestPartnerHistorie.xml",
            additional_context=additional_context,
        )

    def get_verblijfs_titel_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_request(
            "RequestVerblijfsTitelHistorie.xml",
            additional_context=additional_context,
        )

    def get_nationaliteit_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_request(
            "RequestNationaliteitHistorie.xml",
            additional_context=additional_context,
        )