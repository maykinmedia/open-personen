from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from openpersonen.utils.instance_dicts import convert_xml_to_persoon_dicts


class IngeschrevenPersoonViewSet(ViewSet):

    lookup_field = "burgerservicenummer"
    lookup_value_regex = "[0-9]{9}"

    def create(self, request):
        data = convert_xml_to_persoon_dicts(request.body)
        return Response(data=data, status=status.HTTP_200_OK)
