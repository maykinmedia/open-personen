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
        expected_data = convert_xml_to_persoon_dicts(data)

        response = self.client.post(
            reverse("stufbg2api:persoon"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)


class TestOuderView(APITestCase):
    def test_ouder_view(self):
        data = loader.render_to_string("response/ResponseOneOuder.xml")
        expected_data = convert_xml_to_ouder_dict(data)

        response = self.client.post(
            reverse("stufbg2api:ouder"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)


class TestKindView(APITestCase):
    def test_kind_view(self):
        data = loader.render_to_string("response/ResponseOneKind.xml")
        expected_data = convert_xml_to_kind_dict(data)

        response = self.client.post(
            reverse("stufbg2api:kind"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)


class TestPartnerView(APITestCase):
    def test_partner_view(self):
        data = loader.render_to_string("response/ResponseOnePartner.xml")
        expected_data = convert_xml_to_partner_dict(data)

        response = self.client.post(
            reverse("stufbg2api:partner"), data, content_type="application/xml"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
