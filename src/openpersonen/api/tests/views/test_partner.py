from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

import requests_mock
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import (
    PartnerschapFactory,
    PersoonFactory,
    TokenFactory,
)
from openpersonen.api.tests.test_data import PARTNER_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import get_404_response
from openpersonen.contrib.stufbg.models import StufBGClient
from openpersonen.features.country_code_and_omschrijving.factory_models import (
    CountryCodeAndOmschrijvingFactory,
)
from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.factory_models import (
    GemeenteCodeAndOmschrijvingFactory,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)


@patch(
    "openpersonen.api.data_classes.persoon.backend",
    import_string("openpersonen.contrib.stufbg.backend.default"),
)
class TestPartner(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url
        self.persoon_bsn = 123456789
        self.partner_bsn = 987654321
        self.token = TokenFactory.create()
        CountryCodeAndOmschrijvingFactory.create()
        GemeenteCodeAndOmschrijvingFactory.create()

    def test_partner_without_token(self):
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_list_partner(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoPartners.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["partners"]
        self.assertEqual(len(data), 2)
        first_bsn = data[0]["burgerservicenummer"]
        second_bsn = data[1]["burgerservicenummer"]
        self.assertTrue(first_bsn == str(self.partner_bsn) or first_bsn == "123456789")
        self.assertTrue(
            second_bsn == str(self.partner_bsn) or second_bsn == "123456789"
        )

    @requests_mock.Mocker()
    def test_list_partner_with_one_partner(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOnePartner.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["partners"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["burgerservicenummer"], str(self.partner_bsn))

    @requests_mock.Mocker()
    def test_detail_partner(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOnePartner.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.partner_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.maxDiff = None
        self.assertEqual(response.json(), PARTNER_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_partner_BG_response(self, post_mock):
        fake_bsn = 123456780
        fake_partner_bsn = 123456789

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseBG.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": fake_bsn,
                    "id": fake_partner_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json()["burgerservicenummer"], str(fake_partner_bsn))

    @requests_mock.Mocker()
    def test_detail_partner_when_id_does_not_match(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOnePartner.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-detail",
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
    def test_detail_partner_with_two_partners(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoPartners.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.partner_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.maxDiff = None
        self.assertEqual(response.json(), PARTNER_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_partner_when_id_does_not_match_with_two_partners(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoPartners.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 111111111,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(post_mock.called)

    def test_detail_partner_with_bad_id(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "partners-detail",
                    kwargs={
                        "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                        "id": "badid",
                    },
                ),
                HTTP_AUTHORIZATION=f"Token {self.token.key}",
            )


class TestPartnerWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.partner_bsn = 111111111
        self.persoon = PersoonFactory.create(
            burgerservicenummer_persoon=self.persoon_bsn
        )
        self.partnerschap = PartnerschapFactory(
            persoon=self.persoon,
            burgerservicenummer_echtgenoot_geregistreerd_partner=self.partner_bsn,
        )
        self.token = TokenFactory.create()

    def test_partner_without_token(self):
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_partner_with_token(self):
        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_partner(self):

        response = self.client.get(
            reverse(
                "partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["partners"], list))
        data = response.json()["_embedded"]["partners"][0]
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.partner_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"],
            self.partnerschap.voornamen_echtgenoot_geregistreerd_partner,
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.partnerschap.geboortedatum_echtgenoot_geregistreerd_partner),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.geboorteland_echtgenoot_geregistreerd_partner
            ),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.partnerschap.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["datum"][
                "datum"
            ],
            str(
                self.partnerschap.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            ),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["land"][
                "omschrijving"
            ],
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.land_ontbinding_huwelijk_geregistreerd_partnerschap
            ),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["plaats"][
                "omschrijving"
            ],
            GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            ),
        )

    def test_detail_partner(self):

        response = self.client.get(
            reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.partner_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.partner_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"],
            self.partnerschap.voornamen_echtgenoot_geregistreerd_partner,
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.partnerschap.geboortedatum_echtgenoot_geregistreerd_partner),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.geboorteland_echtgenoot_geregistreerd_partner
            ),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.partnerschap.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["datum"][
                "datum"
            ],
            str(
                self.partnerschap.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            ),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["land"][
                "omschrijving"
            ],
            CountryCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.land_ontbinding_huwelijk_geregistreerd_partnerschap
            ),
        )
        self.assertEqual(
            data["_embedded"]["aangaanHuwelijkPartnerschap"]["_embedded"]["plaats"][
                "omschrijving"
            ],
            GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                self.partnerschap.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            ),
        )

    def test_detail_partner_404(self):
        url = reverse(
            "partners-detail",
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
