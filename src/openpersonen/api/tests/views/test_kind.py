from django.template import loader
from django.test import override_settings
from django.urls import reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Kind, Persoon
from openpersonen.api.tests.test_data import KIND_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import response_data_404


@override_settings(USE_STUF_BG_DATABASE=False)
class TestKind(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url

    def test_kind_without_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_kind_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseKind.xml"), encoding="utf-8"
            ),
        )

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), KIND_RETRIEVE_DATA)


@override_settings(USE_STUF_BG_DATABASE=True)
class TestKindWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon = Persoon.objects.create(burgerservicenummer_persoon=000000000)
        self.partnerschap = Kind.objects.create(
            persoon=self.persoon, burgerservicenummer_kind=1
        )

    def test_kind_without_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_kind_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_kind(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["kinderen"], list))
        self.assertEqual(
            response.json()["_embedded"]["kinderen"][0]["burgerservicenummer"], "1"
        )

    def test_detail_kind(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 1},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["burgerservicenummer"], "1")

    def test_detail_kind_404(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": 000000000, "id": 2},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), response_data_404)
