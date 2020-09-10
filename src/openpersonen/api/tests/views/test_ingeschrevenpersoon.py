from django.conf import settings
from django.template import loader
from django.test import TestCase, override_settings
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Persoon
from openpersonen.api.tests.test_data import INGESCHREVEN_PERSOON_RETRIEVE_DATA


@override_settings(USE_STUF_BG_DATABASE=False)
class TestIngeschrevenPersoon(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_no_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse("ingeschrevenpersonen-list"),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    def test_ingeschreven_persoon_without_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + "?burgerservicenummer=123456789&naam__geslachtsnaam==Maykin",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    @requests_mock.Mocker()
    def test_ingeschreven_persoon_with_token_and_proper_query_params(self, post_mock):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=123456789",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_ingeschreven_persoon(self, post_mock):

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": "123456789"},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), INGESCHREVEN_PERSOON_RETRIEVE_DATA)


@override_settings(USE_STUF_BG_DATABASE=True)
class TestIngeschrevenPersoonWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        Persoon.objects.create(burgerservicenummer_persoon=000000000)

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_token_and_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=0",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['_embedded']['ingeschrevenpersonen'][0]['burgerservicenummer'], '0')

    def test_ingeschreven_persoon_with_token_and_incorrect_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=1",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['_embedded']['ingeschrevenpersonen'], [])

    def test_detail_ingeschreven_persoon(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["burgerservicenummer"], "0")
