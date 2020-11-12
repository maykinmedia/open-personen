from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Stufbg2ApiView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        return Response(status=status.HTTP_200_OK)


class Api2StufbgView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request):
        return Response(status=status.HTTP_200_OK)
