from django.core.exceptions import ImproperlyConfigured
from django.template import loader
from django.test import override_settings
from django.urls import reverse
from django.utils.module_loading import import_string

import requests_mock
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import TokenFactory
from openpersonen.contrib.stufbg.models import StufBGClient


class TestPermissions(APITestCase):
    @override_settings(OPENPERSONEN_USE_AUTHENTICATION=True)
    def test_use_authentication_and_use_database(self):
        token = TokenFactory.create()
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @override_settings(OPENPERSONEN_USE_AUTHENTICATION=False)
    def test_not_use_authentication_and_use_database(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789"
        )
        self.assertEqual(response.status_code, 200)

    @override_settings(OPENPERSONEN_USE_AUTHENTICATION=True)
    @requests_mock.Mocker()
    @patch(
        "openpersonen.api.data_classes.persoon.backend",
        import_string("openpersonen.contrib.stufbg.backend.default"),
    )
    def test_use_authentication_and_not_use_database(self, post_mock):
        client_url = StufBGClient.get_solo().url
        api_url = (
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789"
        )
        post_mock.post(
            client_url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        token = TokenFactory.create()
        response = self.client.get(api_url, HTTP_AUTHORIZATION=f"Token {token.key}")
        self.assertEqual(response.status_code, 200)

    @override_settings(
        OPENPERSONEN_USE_AUTHENTICATION=False,
        OPENPERSONEN_BACKEND="openpersonen.contrib.stufbg.backend.default",
    )
    def test_not_use_authentication_and_not_use_database(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(
                reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789"
            )
