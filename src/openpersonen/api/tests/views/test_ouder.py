from django.conf import settings
from django.template import loader
from django.test import override_settings
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Ouder, Persoon
from openpersonen.api.tests.test_data import OUDER_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import response_data_404


@override_settings(USE_STUF_BG_DATABASE=False)
class TestOuder(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url

    def test_ouder_without_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_ouder_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_ouder(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOuder.xml"), encoding="utf-8"
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), OUDER_RETRIEVE_DATA)


@override_settings(USE_STUF_BG_DATABASE=True)
class TestOuderWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon = Persoon.objects.create(burgerservicenummer_persoon=000000000)
        self.partnerschap = Ouder.objects.create(
            persoon=self.persoon, burgerservicenummer_ouder=1
        )

    def test_ouder_without_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_ouder_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_ouder(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["ouders"], list))
        self.assertEqual(
            response.json()["_embedded"]["ouders"][0]["burgerservicenummer"], "1"
        )

    def test_detail_ouder(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["burgerservicenummer"], "1")

    def test_detail_ouder_404(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 2},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), response_data_404)
