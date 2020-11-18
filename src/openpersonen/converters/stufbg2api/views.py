from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from openpersonen.utils.instance_dicts import (
    convert_xml_to_kind_dict,
    convert_xml_to_ouder_dict,
    convert_xml_to_partner_dict,
    convert_xml_to_persoon_dicts,
)


class PersoonView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = convert_xml_to_persoon_dicts(request.body)
        return Response(data=data, status=status.HTTP_200_OK)


class OuderView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = convert_xml_to_ouder_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)


class KindView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = convert_xml_to_kind_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)


class PartnerView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = convert_xml_to_partner_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)
