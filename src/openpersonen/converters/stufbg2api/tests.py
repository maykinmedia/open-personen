from django.template import loader
from django.urls import reverse

from rest_framework.test import APITestCase

from openpersonen.utils.instance_dicts import (
    convert_xml_to_kind_dict,
    convert_xml_to_ouder_dict,
    convert_xml_to_partner_dict,
    convert_xml_to_persoon_dicts,
)


class TestPersoonView(APITestCase):
    def test_persoon_view(self):
        data = loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml")

        response = self.client.post(
            reverse("stufbg2api:ingeschrevenpersonen-list"),
            data,
            content_type="application/xml",
        )

        self.assertEqual(response.status_code, 200)


class TestOuderView(APITestCase):
    def test_ouder_view(self):
        data = loader.render_to_string("response/ResponseOneOuder.xml")

        response = self.client.post(
            reverse("stufbg2api:ouders-list"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)


class TestKindView(APITestCase):
    def test_kind_view(self):
        data = loader.render_to_string("response/ResponseOneKind.xml")

        response = self.client.post(
            reverse("stufbg2api:kinderen-list"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)


class TestPartnerView(APITestCase):
    def test_partner_view(self):
        data = loader.render_to_string("response/ResponseOnePartner.xml")

        response = self.client.post(
            reverse("stufbg2api:partners-list"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)
