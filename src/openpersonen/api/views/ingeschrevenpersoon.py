from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from openpersonen.api.filters.ingeschrevenpersoon import IngeschrevenPersoonFilter
from openpersonen.api.serializers import IngeschrevenPersoonSerializer
from openpersonen.api.test_data import test_data


class IngeschrevenPersoon(ViewSet):

    lookup_field = "burgerservicenummer"
    serializer_class = IngeschrevenPersoonSerializer
    filterset_class = IngeschrevenPersoonFilter

    def list(self, request):

        serializer = IngeschrevenPersoonSerializer(data=test_data, many=True)
        serializer.is_valid()

        return Response(data=serializer.validated_data, status=HTTP_200_OK)

    def retrieve(self, request, burgerservicenummer=None):

        serializer = IngeschrevenPersoonSerializer(data=test_data[0])
        serializer.is_valid()

        return Response(data=serializer.validated_data, status=HTTP_200_OK)
