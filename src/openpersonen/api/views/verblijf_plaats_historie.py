from openpersonen.api.data_classes import VerblijfPlaatsHistorie
from openpersonen.api.serializers import VerblijfPlaatsHistorieSerializer
from openpersonen.api.views.base import HistorieViewSet


class VerblijfPlaatsHistorieViewSet(HistorieViewSet):

    serializer_class = VerblijfPlaatsHistorieSerializer
    instance_class = VerblijfPlaatsHistorie
