from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class IngeschrevenPersoon(ViewSet):

    def list(self, request):
        return Response(data='In list', status=HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response(data=f'In retrieve, pk is {pk}', status=HTTP_200_OK)

