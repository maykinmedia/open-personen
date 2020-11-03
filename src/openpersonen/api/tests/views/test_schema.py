import logging

from django.http import HttpRequest
from django.urls import reverse

from rest_framework.request import Request
from rest_framework.test import APITestCase

from openpersonen.api.schema import info
from openpersonen.api.urls import SchemaView


class TestSchemaView(APITestCase):
    def test_schema_info(self):

        generator = SchemaView().generator_class(
            info, "", "https://testserver.nl", None, None
        )

        #  Disable logging for this function call as it logs a lot of text
        logging.disable(logging.CRITICAL)
        schema = generator.get_schema(Request(request=HttpRequest()), True)
        logging.disable(logging.NOTSET)

        self.assertEqual(schema.info, info)

    def test_schema_view(self):
        response = self.client.get(
            reverse(
                "schema-ingeschreven-persoon",
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Bevragingen ingeschreven personen", str(response.content))

    def test_schema_view_with_format_query_param(self):
        response = self.client.get(
            reverse(
                "schema-ingeschreven-persoon",
            )
            + "?format=openapi"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('"openapi":"3.0.0"', str(response.content))
