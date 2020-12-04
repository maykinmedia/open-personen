from django.test import TestCase

from openpersonen.features.country_code.factory_models import CountryCodeFactory
from openpersonen.features.country_code.models import CountryCode


class TestCountryCode(TestCase):

    def setUp(self):
        super().setUp()
        self.country_code_factory = CountryCodeFactory.create()

    def test_getting_country_omschrijving_by_code(self):
        result = CountryCode.get_omschrijving_from_code(self.country_code_factory.code)
        self.assertEqual(self.country_code_factory.omschrijving, result)

    def test_getting_country_code_by_omschrijving(self):
        result = CountryCode.get_code_from_omschrijving(self.country_code_factory.omschrijving)
        self.assertEqual(self.country_code_factory.code, result)

    def test_getting_country_omschrijving_by_code_returns_Onbekend_when_not_found(self):
        result = CountryCode.get_omschrijving_from_code(99999)
        self.assertEqual('Onbekend', result)

    def test_getting_country_code_by_omschrijving_returns_0_when_not_found(self):
        result = CountryCode.get_code_from_omschrijving('Not found')
        self.assertEqual(0, result)
