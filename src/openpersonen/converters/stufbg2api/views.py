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
    action = "create"
    basename = "ingeschrevenpersonen"

    def post(self, request):
        data = convert_xml_to_persoon_dicts(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request):
        return self.post(request)


class OuderView(APIView):
    action = "create"
    basename = "ouders"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_ouder_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request):
        return self.post(request)


class KindView(APIView):
    action = "create"
    basename = "kinderen"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_kind_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request):
        return self.post(request)


class PartnerView(APIView):
    action = "create"
    basename = "partners"

    def post(self, request):
        self.kwargs["ingeschrevenpersonen_burgerservicenummer"] = 123456789
        data = convert_xml_to_partner_dict(request.body)
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request):
        return self.post(request)
