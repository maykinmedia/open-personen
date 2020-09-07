from openpersonen.api.data_classes import VerblijfsTitelHistorie
from openpersonen.api.serializers import VerblijfsTitelHistorieSerializer
from openpersonen.api.views.base import HistorieViewSet


class VerblijfsTitelHistorieViewSet(HistorieViewSet):

    serializer_class = VerblijfsTitelHistorieSerializer
    instance_class = VerblijfsTitelHistorie
