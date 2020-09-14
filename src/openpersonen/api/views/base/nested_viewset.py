from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from openpersonen.api.views.base import BaseViewSet
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


class NestedViewSet(BaseViewSet):

    lookup_field = "id"
    lookup_value_regex = "[0-9]{9}"

    def list(self, request, *args, **kwargs):
        bsn = kwargs["ingeschrevenpersonen_burgerservicenummer"]

        try:
            instances = self.instance_class.list(bsn)
        except ObjectDoesNotExist:
            return Response(data=RESPONSE_DATA_404, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        bsn = kwargs["ingeschrevenpersonen_burgerservicenummer"]
        id = kwargs["id"]

        try:
            instance = self.instance_class.retrieve(bsn, id)
        except ObjectDoesNotExist:
            return Response(data=RESPONSE_DATA_404, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
