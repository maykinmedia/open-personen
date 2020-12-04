from django.test import TestCase

from openpersonen.features.gemeente_code_and_omschrijving.factory_models import (
    GemeenteCodeAndOmschrijvingFactory,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)


class TestGemeenteAndOmschrijvingCode(TestCase):
    def setUp(self):
        super().setUp()
        self.gemeente_code_and_omschrijving_factory = (
            GemeenteCodeAndOmschrijvingFactory.create()
        )

    def test_getting_gemeente_omschrijving_by_code(self):
        result = GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
            self.gemeente_code_and_omschrijving_factory.code
        )
        self.assertEqual(
            self.gemeente_code_and_omschrijving_factory.omschrijving, result
        )

    def test_getting_gemeente_code_by_omschrijving(self):
        result = GemeenteCodeAndOmschrijving.get_code_from_omschrijving(
            self.gemeente_code_and_omschrijving_factory.omschrijving
        )
        self.assertEqual(self.gemeente_code_and_omschrijving_factory.code, result)

    def test_getting_gemeente_omschrijving_by_code_returns_Onbekend_when_not_found(
        self,
    ):
        result = GemeenteCodeAndOmschrijving.get_omschrijving_from_code(99999)
        self.assertEqual("Onbekend", result)

    def test_getting_gemeente_code_by_omschrijving_returns_0_when_not_found(self):
        result = GemeenteCodeAndOmschrijving.get_code_from_omschrijving("Not found")
        self.assertEqual(0, result)
