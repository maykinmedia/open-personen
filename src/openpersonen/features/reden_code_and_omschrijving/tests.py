from django.test import TestCase

from openpersonen.features.reden_code_and_omschrijving.factory_models import (
    RedenCodeAndOmschrijvingFactory,
)
from openpersonen.features.reden_code_and_omschrijving.models import (
    RedenCodeAndOmschrijving,
)


class TestRedenCodeAndOmschrijving(TestCase):
    def setUp(self):
        super().setUp()
        self.reden_code_and_omschrijving_factory = (
            RedenCodeAndOmschrijvingFactory.create()
        )

    def test_getting_reden_omschrijving_by_code(self):
        result = RedenCodeAndOmschrijving.get_omschrijving_from_code(
            self.reden_code_and_omschrijving_factory.code
        )
        self.assertEqual(self.reden_code_and_omschrijving_factory.omschrijving, result)

    def test_getting_reden_code_by_omschrijving(self):
        result = RedenCodeAndOmschrijving.get_code_from_omschrijving(
            self.reden_code_and_omschrijving_factory.omschrijving
        )
        self.assertEqual(self.reden_code_and_omschrijving_factory.code, result)

    def test_getting_reden_omschrijving_by_code_returns_Onbekend_when_not_found(self):
        result = RedenCodeAndOmschrijving.get_omschrijving_from_code(99999)
        self.assertEqual("Onbekend", result)

    def test_getting_reden_code_by_omschrijving_returns_0_when_not_found(self):
        result = RedenCodeAndOmschrijving.get_code_from_omschrijving("Not found")
        self.assertEqual(".", result)
