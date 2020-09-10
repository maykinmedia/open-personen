from django.conf import settings
from django.template import loader
from django.test import override_settings
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Partnerschap, Persoon
from openpersonen.api.tests.test_data import PARTNER_RETRIEVE_DATA


@override_settings(USE_STUF_BG_DATABASE=False)
class TestPartner(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url

    def test_partner_without_token(self):
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_partner_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_partner(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponsePartner.xml"), encoding="utf-8"
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), PARTNER_RETRIEVE_DATA)


@override_settings(USE_STUF_BG_DATABASE=True)
class TestPartnerWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon = Persoon.objects.create(burgerservicenummer_persoon=000000000)
        self.partnerschap = Partnerschap.objects.create(
            persoon=self.persoon, burgerservicenummer_echtgenoot_geregistreerd_partner=1
        )

    def test_partner_without_token(self):
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_partner_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_partner(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["partners"], list))
        self.assertEqual(
            response.json()["_embedded"]["partners"][0]["burgerservicenummer"], "1"
        )

    def test_detail_partner(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["burgerservicenummer"], "1")
