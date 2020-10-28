from django.test import override_settings

from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import TokenFactory
from openpersonen.api.views.generic_responses import get_404_response


@override_settings(DEBUG=False)
class Test404Response(APITestCase):
    def setUp(self):
        super().setUp()
        self.token = TokenFactory.create()

    def test_default_404_response(self):
        response = self.client.get(
            "/non-existant-endpoint",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertIn("<h1>Not Found</h1>", str(response.content))

    def test_custom_404_response(self):
        response = self.client.get(
            "/api/non-existant-endpoint",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            get_404_response("http://testserver/api/non-existant-endpoint"),
        )
