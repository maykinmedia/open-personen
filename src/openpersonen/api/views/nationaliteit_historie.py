from openpersonen.api.data_classes import NationaliteitHistorie
from openpersonen.api.serializers import NationaliteitHistorieSerializer
from openpersonen.api.views.base import HistorieViewSet


class NationaliteitHistorieViewSet(HistorieViewSet):

    serializer_class = NationaliteitHistorieSerializer
    instance_class = NationaliteitHistorie
