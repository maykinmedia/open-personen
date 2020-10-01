from django.test import TestCase

from openpersonen.api.filters import Backend
from openpersonen.api.views import IngeschrevenPersoonViewSet


class TestFiltersBackend(TestCase):
    def test_get_schema_fields(self):
        self.assertEqual(Backend().get_schema_fields(IngeschrevenPersoonViewSet), [])
