from django.core.exceptions import ObjectDoesNotExist

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from openpersonen.api.views.base import BaseViewSet
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404
from openpersonen.api.views.auto_schema import OpenPersonenAutoSchema


class NestedViewSet(BaseViewSet):

    lookup_field = "id"
    lookup_value_regex = "[0-9]{9}"

    @swagger_auto_schema(auto_schema=OpenPersonenAutoSchema)
    def list(self, request, *args, **kwargs):
        bsn = kwargs["ingeschrevenpersonen_burgerservicenummer"]

        try:
            instances = self.instance_class.list(bsn)
        except ObjectDoesNotExist:
            return Response(data=RESPONSE_DATA_404, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(auto_schema=OpenPersonenAutoSchema)
    def retrieve(self, request, *args, **kwargs):
        bsn = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        id = kwargs["id"]

        try:
            instance = self.instance_class.retrieve(bsn, id)
        except ObjectDoesNotExist:
            return Response(data=RESPONSE_DATA_404, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
