from django.test import TestCase

from openpersonen.features.country_code_and_omschrijving.factory_models import (
    CountryCodeAndOmschrijvingFactory,
)
from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)


class TestCountryAndOmschrijvingCode(TestCase):
    def setUp(self):
        super().setUp()
        self.country_code_and_omschrijving_factory = (
            CountryCodeAndOmschrijvingFactory.create()
        )

    def test_getting_country_omschrijving_by_code(self):
        result = CountryCodeAndOmschrijving.get_omschrijving_from_code(
            self.country_code_and_omschrijving_factory.code
        )
        self.assertEqual(
            self.country_code_and_omschrijving_factory.omschrijving, result
        )

    def test_getting_country_code_by_omschrijving(self):
        result = CountryCodeAndOmschrijving.get_code_from_omschrijving(
            self.country_code_and_omschrijving_factory.omschrijving
        )
        self.assertEqual(self.country_code_and_omschrijving_factory.code, result)

    def test_getting_country_omschrijving_by_code_returns_Onbekend_when_not_found(self):
        result = CountryCodeAndOmschrijving.get_omschrijving_from_code(99999)
        self.assertEqual("Onbekend", result)

    def test_getting_country_code_by_omschrijving_returns_0_when_not_found(self):
        result = CountryCodeAndOmschrijving.get_code_from_omschrijving("Not found")
        self.assertEqual(0, result)
