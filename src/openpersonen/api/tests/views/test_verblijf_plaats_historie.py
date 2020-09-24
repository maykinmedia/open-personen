from django.template import loader
from django.urls import reverse

import requests_mock
from rest_framework.test import APITestCase

from openpersonen.api.models import StufBGClient
from openpersonen.api.tests.factory_models import TokenFactory
from openpersonen.api.tests.test_data import VERBLIJF_PLAATS_HISTORIE_DATA


class TestVerblijfPlaatsHistorie(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url
        self.token = TokenFactory.create()

    def test_verblijf_plaats_historie_without_token(self):
        response = self.client.get(
            reverse(
                "verblijfplaatshistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 123456789},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_verblijf_plaats_historie(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseVerblijfPlaatsHistorie.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "verblijfplaatshistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 123456789},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), VERBLIJF_PLAATS_HISTORIE_DATA)
