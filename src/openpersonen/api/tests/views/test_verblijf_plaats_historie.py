from django.conf import settings
from django.template import loader
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.tests.test_data import verblijf_plaats_historie_data


class TestVerblijfPlaatsHistorie(APITestCase):
    def test_verblijf_plaats_historie_without_token(self):
        response = self.client.get(
            reverse(
                "verblijfplaatshistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_verblijf_plaats_historie(self, post_mock):
        post_mock.post(
            settings.STUF_BG_URL,
            content=bytes(
                loader.render_to_string("ResponseVerblijfPlaatsHistorie.xml"),
                encoding="utf-8",
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "verblijfplaatshistorie-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.maxDiff = None
        self.assertEqual(response.json(), verblijf_plaats_historie_data)