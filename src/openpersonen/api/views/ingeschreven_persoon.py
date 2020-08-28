from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet
from vng_api_common.filters import Backend

from openpersonen.api.data_classes import IngeschrevenPersoon
from openpersonen.api.filters import IngeschrevenPersoonFilter
from openpersonen.api.serializers import IngeschrevenPersoonSerializer


class IngeschrevenPersoonViewSet(ViewSet):

    lookup_field = "burgerservicenummer"
    serializer_class = IngeschrevenPersoonSerializer
    permission_classes = [IsAuthenticated]
    filter_class = IngeschrevenPersoonFilter
    filter_backends = [
        Backend,
    ]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.serializer_class
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        return Response(data=[], status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        burgerservicenummer = kwargs["burgerservicenummer"]

        instance = IngeschrevenPersoon.retrieve(burgerservicenummer)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
