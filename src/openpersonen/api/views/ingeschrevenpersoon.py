from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from openpersonen.api.filters.ingeschrevenpersoon import IngeschrevenPersoonFilter
from openpersonen.api.serializers import IngeschrevenPersoonSerializer


class IngeschrevenPersoon(ViewSet):

    lookup_field = "burgerservicenummer"
    serializer_class = IngeschrevenPersoonSerializer
    filterset_class = IngeschrevenPersoonFilter

    def list(self, request):
        return Response(data='In list', status=HTTP_200_OK)

    def retrieve(self, request, burgerservicenummer=None):
        return Response(data=f'In retrieve, burgerservicenummer is {burgerservicenummer}', status=HTTP_200_OK)
