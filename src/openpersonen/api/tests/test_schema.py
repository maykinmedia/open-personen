from django.http import HttpRequest
from rest_framework.request import Request

from openpersonen.api.schema import info
from rest_framework.test import APITestCase

from openpersonen.api.urls import SchemaView


class TestSchemaView(APITestCase):

    def test_schema_view(self):

        generator = SchemaView().generator_class(info, '', 'https://testserver.nl', None, None)

        schema = generator.get_schema(Request(request=HttpRequest()), True)

        self.assertEqual(schema.info, info)
