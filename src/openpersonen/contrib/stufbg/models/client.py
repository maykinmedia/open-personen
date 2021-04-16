import base64
import uuid
from datetime import timedelta
from io import BytesIO

from django.conf import settings
from django.db import models
from django.template import loader
from django.utils import dateformat, timezone
from django.utils.translation import ugettext_lazy as _

import requests
from lxml import etree
from privates.fields import PrivateMediaFileField
from rest_framework.exceptions import ValidationError
from solo.models import SingletonModel


class StufBGClient(SingletonModel):

    ontvanger_organisatie = models.CharField(
        _("organisatie"), max_length=200, blank=True
    )
    ontvanger_applicatie = models.CharField(_("applicatie"), max_length=200)
    ontvanger_administratie = models.CharField(
        _("administratie"), max_length=200, blank=True
    )
    ontvanger_gebruiker = models.CharField(_("gebruiker"), max_length=200, blank=True)
    zender_organisatie = models.CharField(_("organisatie"), max_length=200, blank=True)
    zender_applicatie = models.CharField(_("applicatie"), max_length=200)
    zender_administratie = models.CharField(
        _("administratie"), max_length=200, blank=True
    )
    zender_gebruiker = models.CharField(_("gebruiker"), max_length=200, blank=True)
    url = models.URLField(
        _("url"),
        blank=True,
        help_text="URL of the StUF-BG service to connect to.",
    )
    user = models.CharField(
        _("user"),
        max_length=200,
        blank=True,
        help_text="Username to use in the XML security context.",
    )
    password = models.CharField(
        _("password"),
        max_length=200,
        blank=True,
        help_text="Password to use in the XML security context.",
    )
    certificate = PrivateMediaFileField(
        upload_to="certificate/",
        blank=True,
        null=True,
        help_text="The SSL certificate file used for client identification. If left empty, mutual TLS is disabled.",
    )
    certificate_key = PrivateMediaFileField(
        upload_to="certificate/",
        help_text="The SSL certificate key file used for client identification. If left empty, mutual TLS is disabled.",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("StUF-BG Client")

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

    def _make_request(self, data):

        cert = (
            (self.certificate.path, self.certificate_key.path)
            if self.certificate and self.certificate_key
            else (None, None)
        )

        with open(
            f"{settings.DJANGO_PROJECT_DIR}/templates/xsds/bg0310/vraagAntwoord/bg0310_namespace.xsd",
            "r",
        ) as f:
            xmlschema_doc = etree.parse(f)
            xmlschema = etree.XMLSchema(xmlschema_doc)

        doc = etree.parse(BytesIO(bytes(data, encoding="UTF-8")))
        el = (
            doc.getroot()
            .xpath(
                "soap:Body",
                namespaces={"soap": "http://schemas.xmlsoap.org/soap/envelope/"},
            )[0]
            .getchildren()[0]
        )
        if not xmlschema.validate(el):
            error_message = xmlschema.error_log.last_error.message
            raise ValidationError(error_message)

        response = requests.post(
            self.url,
            data=data,
            headers=self._get_headers(),
            cert=cert,
        )

        return response

    def _make_historie_request(self, request_file, additional_context):
        request_context = self._get_request_base_context()
        request_context.update(additional_context)

        data = loader.render_to_string(request_file, request_context)

        return self._make_request(data)

    def get_persoon_request_data(self, bsn=None, filters=None):
        context = self._get_request_base_context()
        if bsn:
            context.update({"bsn": bsn})
        if filters:
            context.update(filters)

        template = "request/RequestIngeschrevenPersoon.xml"

        return loader.render_to_string(template, context)

    def get_nested_request_data(self, template, bsn):
        context = self._get_request_base_context()
        context.update({"bsn": bsn})

        return loader.render_to_string(template, context)

    def get_ingeschreven_persoon(self, bsn=None, filters=None):

        data = self.get_persoon_request_data(bsn=bsn, filters=filters)

        return self._make_request(data)

    def get_kind(self, bsn):

        data = self.get_nested_request_data("request/RequestKind.xml", bsn)

        return self._make_request(data)

    def get_ouder(self, bsn):

        data = self.get_nested_request_data("request/RequestOuder.xml", bsn)

        return self._make_request(data)

    def get_partner(self, bsn):

        data = self.get_nested_request_data("request/RequestPartner.xml", bsn)

        return self._make_request(data)

    def get_verblijf_plaats_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_historie_request(
            "request/RequestVerblijfPlaatsHistorie.xml",
            additional_context,
        )

    def get_partner_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_historie_request(
            "request/RequestPartnerHistorie.xml",
            additional_context,
        )

    def get_verblijfs_titel_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_historie_request(
            "request/RequestVerblijfsTitelHistorie.xml",
            additional_context,
        )

    def get_nationaliteit_historie(self, bsn, filters):
        additional_context = {"bsn": bsn}
        additional_context.update(filters)
        return self._make_historie_request(
            "request/RequestNationaliteitHistorie.xml",
            additional_context,
        )
