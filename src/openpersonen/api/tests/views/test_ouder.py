from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

import requests_mock
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import (
    OuderFactory,
    PersoonFactory,
    TokenFactory,
)
from openpersonen.api.tests.test_data import OUDER_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import get_404_response
from openpersonen.contrib.stufbg.models import StufBGClient
from openpersonen.features.country_code_and_omschrijving.factory_models import (
    CountryCodeAndOmschrijvingFactory,
)
from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)


@patch(
    "openpersonen.api.data_classes.persoon.backend",
    import_string("openpersonen.contrib.stufbg.backend.default"),
)
class TestOuder(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.ouder_bsn = 789123456
        self.url = StufBGClient.get_solo().url
        self.token = TokenFactory.create()
        CountryCodeAndOmschrijvingFactory.create()

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
                loader.render_to_string("response/ResponseTwoOuders.xml"),
                encoding="utf-8",
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
                loader.render_to_string("response/ResponseOneOuder.xml"),
                encoding="utf-8",
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
                loader.render_to_string("response/ResponseOneOuder.xml"),
                encoding="utf-8",
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
    def test_detail_ouders_BG_response(self, post_mock):
        fake_bsn = 123456780
        fake_ouder_bsn = 123456790

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseBG.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": fake_bsn,
                    "id": fake_ouder_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json()["burgerservicenummer"], str(fake_ouder_bsn))

    @requests_mock.Mocker()
    def test_detail_ouder_when_id_does_not_match(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneOuder.xml"),
                encoding="utf-8",
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

        self.assertEqual(response.status_code, 404)
        self.assertTrue(post_mock.called)

    @requests_mock.Mocker()
    def test_detail_ouder_with_two_ouders(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoOuders.xml"),
                encoding="utf-8",
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
                loader.render_to_string("response/ResponseTwoOuders.xml"),
                encoding="utf-8",
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

        self.assertEqual(response.status_code, 404)
        self.assertTrue(post_mock.called)

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
        self.token = TokenFactory.create()

    def test_ouder_without_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_ouder_with_token(self):
        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_ouder(self):

        response = self.client.get(
            reverse(
                "ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
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
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.ouder.geboorteland_ouder
            ),
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
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.ouder.geboorteland_ouder
            ),
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
        url = reverse(
            "ouders-detail",
            kwargs={
                "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                "id": 222222222,
            },
        )

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), get_404_response(url))
