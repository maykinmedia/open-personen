from django.template import loader
from django.test import override_settings
from django.urls import NoReverseMatch, reverse

import requests_mock
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.tests.factory_models import OuderFactory, PersoonFactory
from openpersonen.api.tests.test_data import OUDER_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


@override_settings(USE_STUF_BG_DATABASE=False)
class TestOuder(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.ouder_bsn = 789123456
        self.url = StufBGClient.get_solo().url
        self.user = User.objects.create(username="test")
        self.token = Token.objects.create(user=self.user)

    def test_ouder_without_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_list_ouder(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoOuders.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ouders"]
        self.assertEqual(len(data), 2)
        first_bsn = data[0]["burgerservicenummer"]
        second_bsn = data[1]["burgerservicenummer"]
        self.assertTrue(first_bsn == "456123789" or second_bsn == "456123789")
        self.assertTrue(
            first_bsn == str(self.ouder_bsn) or second_bsn == str(self.ouder_bsn)
        )

    @requests_mock.Mocker()
    def test_list_ouder_with_one_ouder(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneOuder.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ouders"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["burgerservicenummer"], str(self.ouder_bsn))

    @requests_mock.Mocker()
    def test_detail_ouder(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneOuder.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.ouder_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), OUDER_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_ouder_when_id_does_not_match(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneOuder.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 111111111,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), dict())

    @requests_mock.Mocker()
    def test_detail_ouder_with_two_ouders(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoOuders.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.ouder_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), OUDER_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_ouder_when_id_does_not_match_with_two_ouders(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoOuders.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 111111111,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), dict())

    def test_detail_ouder_with_bad_id(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "ouders-detail",
                    kwargs={
                        "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                        "id": "badid",
                    },
                ),
                HTTP_AUTHORIZATION=f"Token {self.token.key}",
            )


@override_settings(USE_STUF_BG_DATABASE=True)
class TestOuderWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.ouder_bsn = 111111111
        self.persoon = PersoonFactory.create(
            burgerservicenummer_persoon=self.persoon_bsn
        )
        self.ouder = OuderFactory(
            persoon=self.persoon, burgerservicenummer_ouder=self.ouder_bsn
        )

    def test_ouder_without_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_ouder_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
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
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["ouders"], list))
        data = response.json()["_embedded"]["ouders"][0]
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.ouder_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.ouder.voornamen_ouder
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.ouder.geboortedatum_ouder),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.ouder.geboorteland_ouder),
        )
        self.assertEqual(
            data["_embedded"]["datumIngangFamilierechtelijkeBetrekking"]["datum"],
            str(self.ouder.datum_ingang_familierechtelijke_betrekking_ouder),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.ouder.datum_ingang_onderzoek),
        )

    def test_detail_ouder(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.ouder_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.ouder_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.ouder.voornamen_ouder
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.ouder.geboortedatum_ouder),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.ouder.geboorteland_ouder),
        )
        self.assertEqual(
            data["_embedded"]["datumIngangFamilierechtelijkeBetrekking"]["datum"],
            str(self.ouder.datum_ingang_familierechtelijke_betrekking_ouder),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.ouder.datum_ingang_onderzoek),
        )

    def test_detail_ouder_404(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 222222222,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), RESPONSE_DATA_404)
