from django.test import TestCase

from openpersonen.features import get_gebruik_in_lopende_tekst


class TestGetGebruikInLopendeTekstWithPrefix(TestCase):
    def test_gebruik_in_lopende_tekst_with_prefix(self):
        result = get_gebruik_in_lopende_tekst(
            None, None, None, None, None, None, None, None, None
        )
        self.assertEqual(result, "string")
