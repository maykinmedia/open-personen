from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from openpersonen.api.filters import Backend, HistorieFilter
from openpersonen.api.views.base import BaseViewSet
from openpersonen.api.views.auto_schema import OpenPersonenAutoSchema


class HistorieViewSet(BaseViewSet):
    filter_class = HistorieFilter
    filter_backends = [
        Backend,
    ]

    @swagger_auto_schema(auto_schema=OpenPersonenAutoSchema)
    def list(self, request, *args, **kwargs):
        burgerservicenummer = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        filters = self.filter_class.get_filters_with_values(request)

        instance = self.instance_class.list(burgerservicenummer, filters)

        serializer = self.serializer_class(instance, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)
