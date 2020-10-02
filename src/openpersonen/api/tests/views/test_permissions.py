from django.test import override_settings
from django.urls import reverse

from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import TokenFactory


class TestPermissions(APITestCase):
    @override_settings(USE_STUF_BG_DATABASE=True, USE_AUTHENTICATION=True)
    def test_use_authentication_and_use_database(self):
        token = TokenFactory.create()
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @override_settings(USE_STUF_BG_DATABASE=True, USE_AUTHENTICATION=False)
    def test_not_use_authentication_and_use_database(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789"
        )
        self.assertEqual(response.status_code, 200)

    @override_settings(USE_STUF_BG_DATABASE=True, USE_AUTHENTICATION=True)
    def test_use_authentication_and_not_use_database(self):
        token = TokenFactory.create()
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @override_settings(USE_STUF_BG_DATABASE=False)
    def test_not_use_authentication_and_not_use_database(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789"
        )
        self.assertEqual(response.status_code, 401)
