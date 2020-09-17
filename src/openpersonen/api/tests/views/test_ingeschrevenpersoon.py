from django.template import loader
from django.test import override_settings
from django.urls import NoReverseMatch, reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.tests.factory_models import PersoonFactory
from openpersonen.api.tests.test_data import INGESCHREVEN_PERSOON_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


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
                kwargs={"burgerservicenummer": 123456789},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), INGESCHREVEN_PERSOON_RETRIEVE_DATA)

    def test_detail_ingeschreven_persoon_with_bad_burgerservicenummer(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "ingeschrevenpersonen-detail",
                    kwargs={"burgerservicenummer": "badbsn"},
                ),
                HTTP_AUTHORIZATION=f"Token {token.key}",
            )


@override_settings(USE_STUF_BG_DATABASE=True)
class TestIngeschrevenPersoonWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_token_and_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["_embedded"]["ingeschrevenpersonen"][0][
                "burgerservicenummer"
            ],
            str(self.bsn),
        )

    def test_ingeschreven_persoon_with_token_and_incorrect_proper_query_params(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=1",
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_embedded"]["ingeschrevenpersonen"], [])

    def test_detail_ingeschreven_persoon(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": self.bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["burgerservicenummer"], str(self.bsn))

    def test_not_found_detail_ingeschreven_persoon(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": 111111111},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), RESPONSE_DATA_404)
