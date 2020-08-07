from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from openpersonen.api.serializers import IngeschrevenPersoonSerializer
from openpersonen.api.test_data import test_data


class IngeschrevenPersoon(ReadOnlyModelViewSet):

    lookup_field = "burgerservicenummer"
    serializer_class = IngeschrevenPersoonSerializer

    def list(self, request, *args, **kwargs):

        serializer = IngeschrevenPersoonSerializer(data=test_data, many=True)
        serializer.is_valid()

        return Response(data=serializer.validated_data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        serializer = IngeschrevenPersoonSerializer(data=test_data[0])
        serializer.is_valid()

        return Response(data=serializer.validated_data, status=HTTP_200_OK)
