from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from openpersonen.utils.instance_dicts import (
    convert_xml_to_kind_dict,
    convert_xml_to_ouder_dict,
    convert_xml_to_partner_dict,
    convert_xml_to_persoon_dicts,
)


class PersoonView(APIView):
    action = "list"
    basename = "ingeschrevenpersonen"

    def post(self, request):
        data = convert_xml_to_persoon_dicts(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def list(self, request):
        pass


class OuderView(APIView):
    action = "list"
    basename = "ouders"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_ouder_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def list(self, request):
        pass


class KindView(APIView):
    action = "list"
    basename = "kinderen"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_kind_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def list(self, request):
        pass


class PartnerView(APIView):
    action = "list"
    basename = "partners"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_partner_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def list(self, request):
        pass
