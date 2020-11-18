from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from openpersonen.contrib.stufbg.models import StufBGClient


class NestedViewSet(ViewSet):

    lookup_field = "id"
    lookup_value_regex = "[0-9]{9}"
    backend_template_name = None

    def list(self, request, *args, **kwargs):
        data = StufBGClient.get_solo().get_nested_request_data(
            self.backend_template_name,
            kwargs["ingeschrevenpersonen_burgerservicenummer"],
        )

        return Response(data=data, status=HTTP_200_OK)
