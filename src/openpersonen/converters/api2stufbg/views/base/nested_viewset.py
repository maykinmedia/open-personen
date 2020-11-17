from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from openpersonen.contrib.stufbg.models import StufBGClient


class NestedViewSet(ViewSet):

    lookup_field = "id"
    lookup_value_regex = "[0-9]{9}"

    backend_function_name = None

    def _get_response(self, bsn):
        func = getattr(StufBGClient.get_solo(), self.backend_function_name)

        data = func(bsn=bsn)

        return Response(data=data, status=HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return self._get_response(kwargs["ingeschrevenpersonen_burgerservicenummer"])

    def retrieve(self, request, *args, **kwargs):
        return self._get_response(kwargs["ingeschrevenpersonen_burgerservicenummer"])
