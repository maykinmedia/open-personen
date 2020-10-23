from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

import requests_mock
from freezegun import freeze_time
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import (
    GezagsVerhoudingFactory,
    InschrijvingFactory,
    KiesrechtFactory,
    KindFactory,
    NationaliteitFactory,
    OuderFactory,
    OverlijdenFactory,
    PartnerschapFactory,
    PersoonFactory,
    ReisdocumentFactory,
    TokenFactory,
    VerblijfplaatsFactory,
    VerblijfstitelFactory,
)
from openpersonen.api.tests.test_data import INGESCHREVEN_PERSOON_RETRIEVE_DATA
from openpersonen.api.tests.utils import is_url
from openpersonen.api.views import IngeschrevenPersoonViewSet
from openpersonen.api.views.generic_responses import (
    get_404_response,
    get_expand_400_response,
)
from openpersonen.contrib.stufbg.models import StufBGClient


@patch(
    "openpersonen.api.data_classes.ingeschreven_personen.backend",
    import_string("openpersonen.contrib.stufbg.backend.default"),
)
class TestIngeschrevenPersoon(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url
        self.token = TokenFactory.create()
        self.bsn = 123456789

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_no_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list"),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    def test_ingeschreven_persoon_without_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&naam__geslachtsnaam==Maykin",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    @requests_mock.Mocker()
    def test_ingeschreven_persoon_with_token_and_proper_query_params(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_list_ingeschreven_persoon(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + "?verblijfplaats__identificatiecodenummeraanduiding=A",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ingeschrevenpersonen"]
        self.assertEqual(len(data), 2)

    @requests_mock.Mocker()
    def test_list_ingeschreven_persoon_with_ingeschreven_persoon(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + "?verblijfplaats__identificatiecodenummeraanduiding=A",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ingeschrevenpersonen"]
        self.assertEqual(len(data), 1)

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_detail_ingeschreven_persoon(self, post_mock, is_url_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": self.bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), INGESCHREVEN_PERSOON_RETRIEVE_DATA)

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    def test_detail_ingeschreven_persoon_BG_response(self, post_mock):
        fake_bsn = 123456780

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseBG.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": fake_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json()["burgerservicenummer"], str(fake_bsn))

    def test_detail_ingeschreven_persoon_with_bad_burgerservicenummer(self):
        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "ingeschrevenpersonen-detail",
                    kwargs={"burgerservicenummer": "badbsn"},
                ),
                HTTP_AUTHORIZATION=f"Token {self.token.key}",
            )

    def test_get_filter_parameters(self):
        view = IngeschrevenPersoonViewSet()
        self.assertEqual(view.get_filter_parameters(), [])


class TestIngeschrevenPersoonWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)
        self.gezagsverhouding = GezagsVerhoudingFactory(persoon=self.persoon)
        self.inschrijving = InschrijvingFactory(persoon=self.persoon)
        self.kiesrecht = KiesrechtFactory(persoon=self.persoon)
        self.kind = KindFactory(persoon=self.persoon)
        self.nationaliteit = NationaliteitFactory(persoon=self.persoon)
        self.ouder = OuderFactory(persoon=self.persoon)
        self.overlijden = OverlijdenFactory(persoon=self.persoon)
        self.partnerschap = PartnerschapFactory(persoon=self.persoon)
        self.reisdocument = ReisdocumentFactory(persoon=self.persoon)
        self.verblijfplaats = VerblijfplaatsFactory(persoon=self.persoon)
        self.verblijfstitel = VerblijfstitelFactory(persoon=self.persoon)
        self.token = TokenFactory.create()

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_token_and_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["_embedded"]["inOnderzoek"]["_embedded"][
                "datumIngangOnderzoek"
            ]["datum"],
            str(self.persoon.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.persoon.geboortedatum_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.persoon.geboorteland_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.persoon.geboorteplaats_persoon),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingEuropeesKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_europees_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["datumIngangGeldigheid"][
                "datum"
            ],
            str(self.nationaliteit.datum_van_ingang_geldigheid_met_betrekking),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["nationaliteit"][
                "omschrijving"
            ],
            str(self.nationaliteit.nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["redenOpname"][
                "omschrijving"
            ],
            str(self.nationaliteit.reden_opname_nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.nationaliteit.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["datum"]["datum"],
            str(self.overlijden.datum_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["land"]["omschrijving"],
            str(self.overlijden.land_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["plaats"]["omschrijving"],
            str(self.overlijden.plaats_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["verblijfplaats"]["identificatiecodeNummeraanduiding"],
            self.verblijfplaats.identificatiecode_nummeraanduiding,
        )
        self.assertEqual(
            data["_embedded"]["gezagsverhouding"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.gezagsverhouding.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["reisdocumenten"][0],
            self.reisdocument.nummer_nederlands_reisdocument,
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["aanduiding"][
                "omschrijving"
            ],
            str(self.verblijfstitel.aanduiding_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumEinde"]["datum"],
            str(self.verblijfstitel.datum_einde_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumIngang"]["datum"],
            str(self.verblijfstitel.ingangsdatum_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.verblijfstitel.datum_ingang_onderzoek),
        )

    def test_ingeschreven_persoon_with_token_and_incorrect_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=1",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_embedded"]["ingeschrevenpersonen"], [])

    def test_detail_ingeschreven_persoon(self):
        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": self.bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["_embedded"]["inOnderzoek"]["_embedded"][
                "datumIngangOnderzoek"
            ]["datum"],
            str(self.persoon.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.persoon.geboortedatum_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.persoon.geboorteland_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.persoon.geboorteplaats_persoon),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingEuropeesKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_europees_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["datumIngangGeldigheid"][
                "datum"
            ],
            str(self.nationaliteit.datum_van_ingang_geldigheid_met_betrekking),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["nationaliteit"][
                "omschrijving"
            ],
            str(self.nationaliteit.nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["redenOpname"][
                "omschrijving"
            ],
            str(self.nationaliteit.reden_opname_nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.nationaliteit.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["datum"]["datum"],
            str(self.overlijden.datum_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["land"]["omschrijving"],
            str(self.overlijden.land_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["plaats"]["omschrijving"],
            str(self.overlijden.plaats_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["verblijfplaats"]["identificatiecodeNummeraanduiding"],
            self.verblijfplaats.identificatiecode_nummeraanduiding,
        )
        self.assertEqual(
            data["_embedded"]["gezagsverhouding"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.gezagsverhouding.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["reisdocumenten"][0],
            self.reisdocument.nummer_nederlands_reisdocument,
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["aanduiding"][
                "omschrijving"
            ],
            str(self.verblijfstitel.aanduiding_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumEinde"]["datum"],
            str(self.verblijfstitel.datum_einde_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumIngang"]["datum"],
            str(self.verblijfstitel.ingangsdatum_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.verblijfstitel.datum_ingang_onderzoek),
        )

    def test_not_found_detail_ingeschreven_persoon(self):
        url = reverse(
            "ingeschrevenpersonen-detail",
            kwargs={"burgerservicenummer": 111111111},
        )

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), get_404_response(url))


class TestExpandParameter(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.kind_bsn = 234567891
        self.ouder_bsn = 345678912
        self.partnerschap_bsn = 456789123
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)
        self.kind = KindFactory(
            persoon=self.persoon, burgerservicenummer_kind=self.kind_bsn
        )
        self.ouder = OuderFactory(
            persoon=self.persoon, burgerservicenummer_ouder=self.ouder_bsn
        )
        self.partnerschap = PartnerschapFactory(
            persoon=self.persoon,
            burgerservicenummer_echtgenoot_geregistreerd_partner=self.partnerschap_bsn,
        )
        self.token = TokenFactory.create()

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_expand_parameter_not_included_relatives_not_included(self, is_url_mock):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L45
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

    def test_expand_parameter_errors_when_not_allowed(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L53
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=true"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=true"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=True"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "True"))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=True"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "True"))

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?naam__geslachtsnaam={self.persoon.geslachtsnaam_persoon}&geboorte__datum={self.persoon.geboortedatum_persoon}&expand=true"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

    def test_expand_parameter_errors_with_incorrect_resource(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L66
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=resourcebestaatniet"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "resourcebestaatniet")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=resourcebestaatniet"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "resourcebestaatniet")
        )

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=reisdocumenten"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "reisdocumenten")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=reisdocumenten"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "reisdocumenten")
        )

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=ouders.veldbestaatniet"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "ouders.veldbestaatniet")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=ouders.veldbestaatniet"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "ouders.veldbestaatniet")
        )

    def test_expand_parameter_errors_when_empty(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L80
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand="
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, ""))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand="
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, ""))

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_expand_parameter_with_multiple_resources(self, is_url_mock):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L85
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=partners,kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_embedded"]["kinderen"][0]["burgerservicenummer"], str(self.kind_bsn)
        )
        self.assertEqual(
            data["_embedded"]["partners"][0]["burgerservicenummer"],
            str(self.partnerschap_bsn),
        )
        self.assertIsNone(data.get("ouders"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=partners,kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_embedded"]["kinderen"][0]["burgerservicenummer"], str(self.kind_bsn)
        )
        self.assertEqual(
            data["_embedded"]["partners"][0]["burgerservicenummer"],
            str(self.partnerschap_bsn),
        )
        self.assertIsNone(data.get("ouders"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_expand_parameter_with_dot_notation(self, is_url_mock):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L94
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=ouders.geslachtsaanduiding,ouders.burgerservicenummer",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            self.ouder.geslachtsaanduiding_ouder,
            data["_embedded"]["ouders"]["geslachtsaanduiding"],
        )
        self.assertEqual(
            str(self.ouder.burgerservicenummer_ouder),
            data["_embedded"]["ouders"]["burgerservicenummer"],
        )
        self.assertIsNone(data["_embedded"]["ouders"].get("naam"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geboorte"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geldigVan"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geldigTotEnMet"))
        self.assertIsNone(data["_embedded"]["ouders"].get("_links"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=ouders.geslachtsaanduiding,ouders.burgerservicenummer",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            self.ouder.geslachtsaanduiding_ouder,
            data["_embedded"]["ouders"]["geslachtsaanduiding"],
        )
        self.assertEqual(
            str(self.ouder.burgerservicenummer_ouder),
            data["_embedded"]["ouders"]["burgerservicenummer"],
        )
        self.assertIsNone(data["_embedded"]["ouders"].get("naam"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geboorte"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geldigVan"))
        self.assertIsNone(data["_embedded"]["ouders"].get("geldigTotEnMet"))
        self.assertIsNone(data["_embedded"]["ouders"].get("_links"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_expand_parameter_with_dot_notation_of_entire_data_group(self, is_url_mock):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L110
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=kinderen.naam,kinderen.geboorte",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voorvoegsel"],
            self.kind.voorvoegsel_geslachtsnaam_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"][
                "datum"
            ]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"]["land"][
                "omschrijving"
            ],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"][
                "plaats"
            ]["omschrijving"],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_embedded"].get("burgerservicenummer")
        )
        self.assertIsNone(data["_embedded"]["kinderen"]["_embedded"].get("geldigVan"))
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_embedded"].get("geldigTotEnMet")
        )
        self.assertIsNone(data["_embedded"]["kinderen"]["_embedded"].get("_links"))
        self.assertIsNone(data["_embedded"].get("ouders"))
        self.assertIsNone(data["_embedded"].get("partners"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=kinderen.naam,kinderen.geboorte",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voorvoegsel"],
            self.kind.voorvoegsel_geslachtsnaam_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"][
                "datum"
            ]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"]["land"][
                "omschrijving"
            ],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["geboorte"]["_embedded"][
                "plaats"
            ]["omschrijving"],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_embedded"].get("burgerservicenummer")
        )
        self.assertIsNone(data["_embedded"]["kinderen"]["_embedded"].get("geldigVan"))
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_embedded"].get("geldigTotEnMet")
        )
        self.assertIsNone(data["_embedded"]["kinderen"]["_embedded"].get("_links"))
        self.assertIsNone(data["_embedded"].get("ouders"))
        self.assertIsNone(data["_embedded"].get("partners"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_expand_parameter_with_dot_notation_of_portion_of_data_group(
        self, is_url_mock
    ):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L128
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertIsNotNone(data["_embedded"]["kinderen"]["_links"])
        self.assertIsNone(data.get("ouders"))
        self.assertIsNone(data.get("partners"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertIsNotNone(data["_embedded"]["kinderen"]["_links"])
        self.assertIsNone(data.get("ouders"))
        self.assertIsNone(data.get("partners"))
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

    @patch("djangorestframework_hal.utils.is_url", side_effect=is_url)
    def test_links_of_expand_parameter_with_dot_notation_of_portion_of_data_group(
        self, is_url_mock
    ):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L142
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_links"].get("ingeschrevenpersonen")
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertIsNotNone(data["_embedded"]["kinderen"]["_links"]["self"])
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsNone(
            data["_embedded"]["kinderen"]["_links"].get("ingeschrevenpersonen")
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertIsNotNone(data["_embedded"]["kinderen"]["_links"]["self"])
        self.assertEqual(
            data["_links"]["partners"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/partners/{self.partnerschap_bsn}",
        )
        self.assertEqual(
            data["_links"]["ouders"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/ouders/{self.ouder_bsn}",
        )
        self.assertEqual(
            data["_links"]["kinderen"][0]["_links"]["self"]["href"],
            f"http://testserver/api/ingeschrevenpersonen/{self.bsn}/kinderen/{self.kind_bsn}",
        )


class TestFieldParameter(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.kind_bsn = 234567891
        self.ouder_bsn = 345678912
        self.partnerschap_bsn = 456789123
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)
        self.kind = KindFactory(
            persoon=self.persoon, burgerservicenummer_kind=self.kind_bsn
        )
        self.ouder = OuderFactory(
            persoon=self.persoon, burgerservicenummer_ouder=self.ouder_bsn
        )
        self.partnerschap = PartnerschapFactory(
            persoon=self.persoon,
            burgerservicenummer_echtgenoot_geregistreerd_partner=self.partnerschap_bsn,
        )
        self.token = TokenFactory.create()

    def test_fields_parameter_not_included(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L46
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(
            data["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_links"]["ouders"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/ouders",
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(
            data["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_links"]["ouders"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/ouders",
        )

    def test_one_attribute_being_requested(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L52
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=geslachtsaanduiding",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNotNone(data["_links"].get("self"))
        self.assertEqual(
            data["geslachtsaanduiding"], str(self.persoon.geslachtsaanduiding)
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=geslachtsaanduiding",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNotNone(data["_links"].get("self"))
        self.assertEqual(
            data["geslachtsaanduiding"], str(self.persoon.geslachtsaanduiding)
        )

    def test_multiple_attributes_being_requested(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L57
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=burgerservicenummer,geslachtsaanduiding",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data["_links"]), 4)
        self.assertEqual(
            data["burgerservicenummer"], str(self.persoon.burgerservicenummer_persoon)
        )
        self.assertEqual(
            data["geslachtsaanduiding"], str(self.persoon.geslachtsaanduiding)
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=burgerservicenummer,geslachtsaanduiding",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNotNone(data["_links"].get("self"))
        self.assertEqual(
            data["burgerservicenummer"], str(self.persoon.burgerservicenummer_persoon)
        )
        self.assertEqual(
            data["geslachtsaanduiding"], str(self.persoon.geslachtsaanduiding)
        )

    def test_fields_with_group_being_requested(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L62
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=burgerservicenummer,naam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data["_links"]), 4)
        self.assertEqual(
            data["burgerservicenummer"], str(self.persoon.burgerservicenummer_persoon)
        )
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["aanduidingNaamgebruik"],
            self.persoon.aanduiding_naamgebruik,
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=burgerservicenummer,naam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNotNone(data["_links"].get("self"))
        self.assertEqual(
            data["burgerservicenummer"], str(self.persoon.burgerservicenummer_persoon)
        )
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["aanduidingNaamgebruik"],
            self.persoon.aanduiding_naamgebruik,
        )

    def test_fields_with_attributes_of_group_being_requested(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L62
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=naam.voorvoegsel,naam.voornamen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNone(data["_embedded"]["naam"].get("geslachtsnaam"))
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )
        self.assertIsNone(data["_embedded"]["naam"].get("aanduidingNaamgebruik"))

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=naam.voorvoegsel,naam.voornamen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data["_links"]), 4)
        self.assertIsNotNone(data["_links"].get("self"))
        self.assertIsNone(data["_embedded"]["naam"].get("geslachtsnaam"))
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )
        self.assertIsNone(data["_embedded"]["naam"].get("aanduidingNaamgebruik"))

    def test_fields_with__links_attribute(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L74
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=burgerservicenummer,naam,_links.partners",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data["_links"]), 2)
        self.assertEqual(
            data["_links"]["self"]["href"],
            "http://testserver.com/api/ingeschrevenpersonen",
        )
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertIsInstance(data["_embedded"]["naam"], dict)

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=burgerservicenummer,naam,_links.partners",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["_links"]), 2)
        self.assertEqual(
            data["_links"]["self"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}",
        )
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertIsInstance(data["_embedded"]["naam"], dict)

    def test_fields_with_expand_attribute(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L80
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=geboorte.land&expand=kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data["_embedded"]["geboorte"]), 1)
        self.assertEqual(len(data["_embedded"]["geboorte"]["_embedded"]), 1)
        self.assertEqual(len(data["_embedded"]["geboorte"]["_embedded"]["land"]), 2)
        kind = data["_embedded"]["kinderen"][0]
        self.assertEqual(len(kind["_links"]), 1)
        self.assertEqual(
            kind["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(kind["burgerservicenummer"], str(self.kind_bsn))
        self.assertEqual(len(kind["_embedded"]["naam"]), 5)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["datum"]), 4)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["plaats"]), 2)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["land"]), 2)

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=geboorte.land&expand=kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["_embedded"]["geboorte"]), 1)
        self.assertEqual(len(data["_embedded"]["geboorte"]["_embedded"]), 1)
        self.assertEqual(len(data["_embedded"]["geboorte"]["_embedded"]["land"]), 2)
        kind = data["_embedded"]["kinderen"][0]
        self.assertEqual(len(kind["_links"]), 1)
        self.assertEqual(
            kind["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(kind["burgerservicenummer"], str(self.kind_bsn))
        self.assertEqual(len(kind["_embedded"]["naam"]), 5)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["datum"]), 4)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["plaats"]), 2)
        self.assertEqual(len(kind["_embedded"]["geboorte"]["_embedded"]["land"]), 2)

    def test_fields_links_with_expand_attribute(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L92
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=_links.partners&expand=kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(len(data["_links"]), 2)
        self.assertEqual(
            data["_links"]["self"]["href"],
            "http://testserver.com/api/ingeschrevenpersonen",
        )
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(len(data["_embedded"]), 1)
        self.assertIsInstance(data["_embedded"]["kinderen"], list)

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=_links.partners&expand=kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["_links"]), 2)
        self.assertEqual(
            data["_links"]["self"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}",
        )
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(len(data["_embedded"]), 1)
        self.assertIsInstance(data["_embedded"]["kinderen"], list)

    def test_fields_links_with_expand_dot_attribute(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/fields.feature#L92
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&fields=burgerservicenummer,naam,geboorte&expand=kinderen.naam.voornamen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(len(data["_embedded"]), 3)
        self.assertIsInstance(data["_embedded"]["naam"], dict)
        self.assertIsInstance(data["_embedded"]["geboorte"], dict)
        self.assertEqual(len(data["_embedded"]["kinderen"]["_embedded"]["naam"]), 1)
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(len(data["_embedded"]["kinderen"]["_links"]["self"]), 1)
        self.assertEqual(
            data["_embedded"]["kinderen"]["_links"]["self"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?fields=burgerservicenummer,naam,geboorte&expand=kinderen.naam.voornamen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(len(data["_embedded"]), 3)
        self.assertIsInstance(data["_embedded"]["naam"], dict)
        self.assertIsInstance(data["_embedded"]["geboorte"], dict)
        self.assertEqual(len(data["_embedded"]["kinderen"]["_embedded"]["naam"]), 1)
        self.assertEqual(
            data["_embedded"]["kinderen"]["_embedded"]["naam"]["voornamen"],
            self.kind.voornamen_kind,
        )
        self.assertEqual(len(data["_embedded"]["kinderen"]["_links"]["self"]), 1)
        self.assertEqual(
            data["_embedded"]["kinderen"]["_links"]["self"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.persoon.voornamen_persoon
        )
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voorvoegsel"],
            self.persoon.voorvoegsel_geslachtsnaam_persoon,
        )
