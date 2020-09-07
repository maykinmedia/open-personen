from openpersonen.api.data_classes import PartnerHistorie
from openpersonen.api.serializers import PartnerHistorieSerializer
from openpersonen.api.views.base import HistorieViewSet


class PartnerHistorieViewSet(HistorieViewSet):

    serializer_class = PartnerHistorieSerializer
    instance_class = PartnerHistorie
