from django.test import override_settings
from django.urls import reverse

from rest_framework.test import APITestCase


class TestPersoonView(APITestCase):
    def test_persoon_view(self):
        response = self.client.post(reverse("stufbg2api:persoon"))
        self.assertEqual(response.status_code, 200)


class TestOuderView(APITestCase):
    def test_ouder_view(self):
        response = self.client.post(reverse("stufbg2api:ouder"))
        self.assertEqual(response.status_code, 200)


class TestKindView(APITestCase):
    def test_kind_view(self):
        response = self.client.post(reverse("stufbg2api:kind"))
        self.assertEqual(response.status_code, 200)


class TestPartnerView(APITestCase):
    def test_partner_view(self):
        response = self.client.post(reverse("stufbg2api:partner"))
        self.assertEqual(response.status_code, 200)
