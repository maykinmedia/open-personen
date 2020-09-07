from django.template import loader
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.tests.test_data import NATIONALITEIT_HISTORIE_DATA
from openpersonen.api.models import StufBGClient

class TestNationaliteitHistorie(APITestCase):

    def setUp(self):
        self.url = StufBGClient.get_solo().url

    def test_nationaliteit_historie_without_token(self):
        response = self.client.get(
            reverse(
                "nationaliteithistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_nationaliteit_historie(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseNationaliteitHistorie.xml"),
                encoding="utf-8",
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "nationaliteithistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), NATIONALITEIT_HISTORIE_DATA)
