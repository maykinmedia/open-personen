from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from openpersonen.api.filters import Backend, HistorieFilter
from openpersonen.api.views.base import BaseViewSet


class HistorieViewSet(BaseViewSet):
    filter_class = HistorieFilter
    filter_backends = [
        Backend,
    ]

    def list(self, request, *args, **kwargs):
        burgerservicenummer = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        filters = self.filter_class.get_filters_with_values(request)

        instance = self.instance_class.list(burgerservicenummer, filters)

        serializer = self.serializer_class(instance, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)
