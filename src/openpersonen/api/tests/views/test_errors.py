from django.test import override_settings

from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import TokenFactory


@override_settings(DEBUG=False)
class Test404Response(APITestCase):
    def test_default_404_response(self):
        response = self.client.get(
            "/non-existant-endpoint",
            HTTP_AUTHORIZATION=f"Token {TokenFactory.create().key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertIn("<h1>Not Found</h1>", str(response.content))

    def test_custom_404_response(self):
        response = self.client.get(
            "/api/non-existant-endpoint",
            HTTP_AUTHORIZATION=f"Token {TokenFactory.create().key}",
        )

        self.assertEqual(response.status_code, 404)
        json_response = response.json()
        self.assertEqual(
            json_response["type"],
            "https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#/10.4.5 404 Not Found",
        )
        self.assertEqual(json_response["title"], "Opgevraagde resource bestaat niet.")
        self.assertEqual(json_response["status"], 404)
        self.assertEqual(
            json_response["detail"],
            "The server has not found anything matching the Request-URI.",
        )
        self.assertEqual(
            json_response["instance"], "http://testserver/api/non-existant-endpoint"
        )
        self.assertEqual(json_response["code"], "notFound")
