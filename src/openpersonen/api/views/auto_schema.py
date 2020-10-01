from django.utils.translation import gettext_lazy as _

from drf_yasg import openapi
from vng_api_common.inspectors.view import HTTP_STATUS_CODE_TITLES, AutoSchema
from vng_api_common.serializers import FoutSerializer, ValidatieFoutSerializer


class OpenPersonenAutoSchema(AutoSchema):
    def _get_error_responses(self):
        responses = super()._get_error_responses()

        responses[400] = openapi.Response(
            description=HTTP_STATUS_CODE_TITLES[400],
            schema=self.serializer_to_schema(ValidatieFoutSerializer()),
        )

        for status_code in [401, 403, 404, 406, 409, 410, 415, 429, 500, 501, 503]:
            responses[status_code] = openapi.Response(
                description=HTTP_STATUS_CODE_TITLES[status_code],
                schema=self.serializer_to_schema(FoutSerializer()),
            )

        responses["default"] = openapi.Response(
            description=_("Er is een onverwachte fout opgetreden"),
            schema=self.serializer_to_schema(FoutSerializer()),
        )

        return responses
