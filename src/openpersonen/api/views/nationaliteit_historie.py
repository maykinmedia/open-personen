from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet
from vng_api_common.filters import Backend

from openpersonen.api.data_classes import NationaliteitHistorie
from openpersonen.api.filters import HistorieFilter
from openpersonen.api.serializers import NationaliteitHistorieSerializer


class NationaliteitHistorieViewSet(ViewSet):

    filter_class = HistorieFilter
    filter_backends = [
        Backend,
    ]
    serializer_class = NationaliteitHistorieSerializer
    permission_classes = [IsAuthenticated]

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
        burgerservicenummer = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        filters = self.filter_class.get_filters_with_values(request)

        instance = NationaliteitHistorie.list(burgerservicenummer, filters)

        serializer = self.serializer_class(instance, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)
