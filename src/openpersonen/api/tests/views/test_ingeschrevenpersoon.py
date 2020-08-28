from django.conf import settings
from django.template import loader
from django.urls import reverse

import requests_mock
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.tests.test_data import ingeschreven_persoon_retrieve_data
from openpersonen.api.views import IngeschrevenPersoonViewSet


class TestIngeschrevenPersoon(APITestCase):
    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_without_proper_query_params(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('ingeschrevenpersonen-list'), HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['detail'], 'Incorrect combination of filters')

    def test_ingeschreven_persoon_with_token_and_proper_query_params(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('ingeschrevenpersonen-list') + '?burgerservicenummer=123456789',
                                   HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_ingeschreven_persoon(self, post_mock):

        post_mock.post(
            settings.STUF_BG_URL,
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
        self.assertEqual(response.json(), ingeschreven_persoon_retrieve_data)


class TestCombinations(TestCase):

    def test_combination_1_returns_true(self):
        test_dict = {
            'geboorte__datum': '20010119',
            'naam__geslachtsnaam': 'Maykin'
        }

        result = IngeschrevenPersoonViewSet.combination_1(test_dict)

        self.assertTrue(result)

    def test_combination_1_returns_when_geboorte__datum_missing(self):
        test_dict = {
            'naam__geslachtsnaam': 'Maykin'
        }

        result = IngeschrevenPersoonViewSet.combination_1(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('naam__geslachtsnaam'))

    def test_combination_1_returns_when_naam__geslachtsnaam_missing(self):
        test_dict = {
            'geboorte__datum': '20010119'
        }

        result = IngeschrevenPersoonViewSet.combination_1(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('geboorte__datum'))

    def test_combination_2_returns_true(self):
        test_dict = {
            'verblijfplaats__gemeentevaninschrijving': 'Amsterdam',
            'naam__geslachtsnaam': 'Maykin'
        }

        result = IngeschrevenPersoonViewSet.combination_2(test_dict)

        self.assertTrue(result)

    def test_combination_2_returns_when_verblijfplaats__gemeentevaninschrijving_missing(self):
        test_dict = {
            'naam__geslachtsnaam': 'Maykin'
        }

        result = IngeschrevenPersoonViewSet.combination_2(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('naam__geslachtsnaam'))

    def test_combination_2_returns_when_naam__geslachtsnaam_missing(self):
        test_dict = {
            'verblijfplaats__gemeentevaninschrijving': 'Amsterdam'
        }

        result = IngeschrevenPersoonViewSet.combination_2(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__gemeentevaninschrijving'))

    def test_combination_3_returns_true(self):
        test_dict = {
            'burgerservicenummer': '123456789'
        }

        result = IngeschrevenPersoonViewSet.combination_3(test_dict)

        self.assertTrue(result)

    def test_combination_3_returns_false(self):
        test_dict = {
            'not_burgerservicenummer': 'abcd'
        }

        result = IngeschrevenPersoonViewSet.combination_3(test_dict)

        self.assertFalse(result)

    def test_combination_4_returns_true(self):
        test_dict = {
            'verblijfplaats__postcode': '9VGM3H',
            'verblijfplaats__huisnummer': 117
        }

        result = IngeschrevenPersoonViewSet.combination_4(test_dict)

        self.assertTrue(result)

    def test_combination_4_returns_when_verblijfplaats__huisnummer_missing(self):
        test_dict = {
            'verblijfplaats__postcode': '9VGM3H'
        }

        result = IngeschrevenPersoonViewSet.combination_4(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__postcode'))

    def test_combination_4_returns_when_verblijfplaats__postcode_missing(self):
        test_dict = {
            'verblijfplaats__huisnummer': 117
        }

        result = IngeschrevenPersoonViewSet.combination_4(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__huisnummer'))

    def test_combination_5_returns_true(self):
        test_dict = {
            'verblijfplaats__naamopenbareruimte': 'Jordaan',
            'verblijfplaats__gemeentevaninschrijving': 'Amsterdam',
            'verblijfplaats__huisnummer': 117
        }

        result = IngeschrevenPersoonViewSet.combination_5(test_dict)

        self.assertTrue(result)

    def test_combination_5_returns_when_verblijfplaats__huisnummer_missing(self):
        test_dict = {
            'verblijfplaats__naamopenbareruimte': 'Jordaan',
            'verblijfplaats__gemeentevaninschrijving': 'Amsterdam'
        }

        result = IngeschrevenPersoonViewSet.combination_5(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__naamopenbareruimte'))
        self.assertIsNone(test_dict.get('verblijfplaats__gemeentevaninschrijving'))

    def test_combination_5_returns_when_verblijfplaats__gemeentevaninschrijving_missing(self):
        test_dict = {
            'verblijfplaats__naamopenbareruimte': 'Jordaan',
            'verblijfplaats__huisnummer': 117
        }

        result = IngeschrevenPersoonViewSet.combination_5(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__naamopenbareruimte'))
        self.assertIsNone(test_dict.get('verblijfplaats__huisnummer'))

    def test_combination_5_returns_when_verblijfplaats__naamopenbareruimte_missing(self):
        test_dict = {
            'verblijfplaats__gemeentevaninschrijving': 'Amsterdam',
            'verblijfplaats__huisnummer': 117
        }

        result = IngeschrevenPersoonViewSet.combination_5(test_dict)

        self.assertFalse(result)
        self.assertIsNone(test_dict.get('verblijfplaats__gemeentevaninschrijving'))
        self.assertIsNone(test_dict.get('verblijfplaats__huisnummer'))

    def test_combination_6_returns_true(self):
        test_dict = {
            'verblijfplaats__identificatiecodenummeraanduiding': 'AB'
        }

        result = IngeschrevenPersoonViewSet.combination_6(test_dict)

        self.assertTrue(result)

    def test_combination_6_returns_false(self):
        test_dict = {
            'not_verblijfplaats__identificatiecodenummeraanduiding': 'AB'
        }

        result = IngeschrevenPersoonViewSet.combination_6(test_dict)

        self.assertFalse(result)
