from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from openpersonen.utils.instance_dicts import convert_xml_to_partner_dict


class PartnerViewSet(ViewSet):
    def create(self, request, *args, **kwargs):
        data = convert_xml_to_partner_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)
