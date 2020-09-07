from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from openpersonen.api.views.base import BaseViewSet


class NestedViewSet(BaseViewSet):

    def list(self, request, *args, **kwargs):
        return Response(data=[], status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        burgerservicenummer = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        id = kwargs["id"]

        instance = self.instance_class.retrieve(burgerservicenummer)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
